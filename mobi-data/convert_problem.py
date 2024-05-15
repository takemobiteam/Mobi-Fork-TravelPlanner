import json
from definitions import *
from serializer import CustomEncoder
from datetime import datetime, timedelta

DAY_DURATION = 24 * 60 * 60 # 1 day

ACTIVITY_DURATION = 60 * 60 # 1 hour
ACTIVITY_UTILITY = 50 # Base utility
ACTIVITY_START_TIME = 9 * 60 * 60 # 9:00 AM
ACTIVITY_END_TIME = 18 * 60 * 60 # 6:00 PM

DINING_DURATION = 60 * 60 # 1 hour
RESTAURANT_UTILITY_SCALING = 15 # Scaled by ratings
BREAKFAST_START_TIME = 8 * 60 * 60 # 8:00 AM
BREAKFAST_END_TIME = 10 * 60 * 60 # 10:00 AM
LUNCH_START_TIME = 12 * 60 * 60 # 12:00 PM
LUNCH_END_TIME = 14 * 60 * 60 # 2:00 PM
DINNER_START_TIME = 18 * 60 * 60 # 6:00 PM
DINNER_END_TIME = 20 * 60 * 60 # 8:00 PM

HOTEL_BASE_DURATION = 60 * 60 # 1 hour
HOTEL_UTILITY_SCALING = 20 # Scaled by ratings
HOTEL_VISIT_UTILITY = 100
HOTEL_CHECKIN_TIME = 15 * 60 * 60 # 3:00 PM
HOTEL_CHECKOUT_TIME = 12 * 60 * 60 # 12:00 PM
HOTEL_PREFERRED_START_TIME = 21 * 60 * 60 # 9:00 PM

USE_REAL_LAT_LON = False
FAKE_LAT = 0.0
FAKE_LON = 0.0
DEFAULT_LAT = 42.2773242
DEFAULT_LON = -89.08814249

def load_jsonl(file_path):
    all_data = []
    with open(file_path, 'r') as f:
        for line in f:
            all_data.append(json.loads(line))
    return all_data

def convert_problem(data):
    # Dates of the problem
    days = data['days']
    dates = list(map(get_datetime_from_string, data['date']))
    end_datetime = dates[0] + timedelta(days=days)

    # Create problem with start and end events
    start_event = Event()
    end_event = Event()
    start_event.scheduled_time = dates[0]
    problem = Problem(start_event, end_event)

    # Add user_start and end events
    user_start = Event()
    user_end = Event()
    problem.add_episode(start_event, user_start, 0, None)
    problem.add_episode(user_end, end_event, 0, None)
    # TODO: a different user_start lb??
    user_start.earliest_time = dates[0]
    problem.add_episode(start_event, user_start, 0, None)
    user_end.latest_time = end_datetime
    problem.add_episode(start_event, user_end, 0, DAY_DURATION * days)

    # Obtain origin
    origin = data['org']
    destination = data['dest']
    # TODO: add origin location
    if USE_REAL_LAT_LON:
        origin_loc = problem.add_location(origin, DEFAULT_LAT, DEFAULT_LON)
    else:
        origin_loc = problem.add_location(origin, FAKE_LAT, FAKE_LON)

    # Create user agent with round trip
    agent = Agent(user_start, user_end, origin_loc, origin_loc)
    problem.add_agent(agent)

    # Go through each activity in the problem and construct goal groups
    for info in data['structured_ref_info']:
        if info['Info Type'] == 'Attractions':
            goal_groups = add_activities(info, problem, user_start, user_end, dates)
            for goal_group in goal_groups:
                agent.add_goal_group(goal_group)
        elif info['Info Type'] == 'Restaurants':
            goal_groups = add_restaurants(info, problem, user_start, user_end, dates)
            for goal_group in goal_groups:
                agent.add_goal_group(goal_group)
        elif info['Info Type'] == 'Accommodations':
            goal_groups = add_hotels(info, problem, start_event, user_start, user_end, dates)
            for goal_group in goal_groups:
                agent.add_goal_group(goal_group)


    return problem

def add_activities(info, problem, user_start, user_end, dates):
    num_activities = info['Number']
    info_data = info['Structured Content']
    names = info_data['Name']
    lats = info_data['Latitude']
    lons = info_data['Longitude']
    addresses = info_data['Address']
    phones = info_data['Phone']
    websites = info_data['Website']
    cities = info_data['City']

    goal_groups = []

    for idx in range(num_activities):
        i = str(idx)
        arrival_event = Event()
        start_event = Event()
        end_event = Event()
        departure_event = Event()

        # Add constraint episodes
        ep1 = problem.add_episode(user_start, arrival_event, 0, None)
        ep2 = problem.add_episode(arrival_event, start_event, 0, None)
        ep3 = problem.add_episode(start_event, end_event, 1, None)
        ep4 = problem.add_episode(end_event, departure_event, 0, None)
        ep5 = problem.add_episode(departure_event, user_end, 0, None)
        ep6 = problem.add_episode(arrival_event, departure_event, 0, None)

        # Add activity episode
        activity = problem.add_episode(start_event, end_event,
                                       ACTIVITY_DURATION, ACTIVITY_DURATION, True)
        activity.name = names[i]
        if USE_REAL_LAT_LON:
            location = problem.add_location(names[i], lats[i], lons[i])
        else:
            location = problem.add_location(names[i], FAKE_LAT, FAKE_LON)
        activity.start_location = location
        activity.end_location = location
        activity.time_windows = get_activity_time_windows(dates)

        # Add decision variable for choice of activity, guards 1 episode
        choice_var = problem.add_decision_variable('Choice_' + names[i],
                                                   {names[i]: ACTIVITY_UTILITY})
        choice = choice_var.get_assignment(names[i])
        activity.add_guard(choice)

        # Add decision variable for visit or not, guards 6 episodes, 1 goal group, 1 variable
        visit_var = problem.add_decision_variable('IncludeOrNot_' + names[i],
                                                  {"Visit": 0.0, "NotVisit": 0.0})
        visit = visit_var.get_assignment('Visit')
        for obj in [ep1, ep2, ep3, ep4, ep5, ep6, choice_var]:
            obj.add_guard(visit)

        # Add goal group
        goal_group = problem.add_goal_group(names[i], start_event, end_event,
                                            arrival_event, departure_event, 100)
        goal_group.add_goal_episode(activity)
        goal_group.selection_variable = choice_var
        goal_group.add_guard(visit)

        goal_groups.append(goal_group)

    return goal_groups


def add_restaurants(info, problem, user_start, user_end, dates):
    num_restaurants = info['Number']
    info_data = info['Structured Content']
    names = info_data['Name']
    costs = info_data['Average Cost']
    cuisines = info_data['Cuisines']
    ratings = info_data['Aggregate Rating']
    cities = info_data['City']

    goal_groups = []

    # Create breakfast, lunch and dinner goals for each day
    # where each goal group has a choice of different restaurants
    for meal in ['Breakfast', 'Lunch', 'Dinner']:
        for date in dates:
            goal = add_restaurant_goal_group(problem, user_start, user_end, meal, date,
                                             num_restaurants, names, costs, cuisines,
                                             ratings, cities)
            goal_groups.append(goal)


    # Add all diff constraint so that no restaurant is repeated
    all_diff = AllDiff()
    for goal_group in goal_groups:
        all_diff.add_variable(goal_group.selection_variable)
    for name in names:
        all_diff.add_domain_value(name)
    problem.add_global_constraint(all_diff)

    return goal_groups


def add_restaurant_goal_group(problem, user_start, user_end, meal, date,
                              num_restaurants, names, costs, cuisines,
                              ratings, cities):
    # TODO: add costs, filter cuisine
    arrival_event = Event()
    start_event = Event()
    end_event = Event()
    departure_event = Event()

    # Add constraint episodes
    ep1 = problem.add_episode(user_start, arrival_event, 0, None)
    ep2 = problem.add_episode(arrival_event, start_event, 0, None)
    ep3 = problem.add_episode(start_event, end_event, 1, None)
    ep4 = problem.add_episode(end_event, departure_event, 0, None)
    ep5 = problem.add_episode(departure_event, user_end, 0, None)
    ep6 = problem.add_episode(arrival_event, departure_event, 0, None)

    # Add goal group
    goal_group = problem.add_goal_group(meal+"-"+date.strftime('%m/%d'),
                                        start_event, end_event,
                                        arrival_event, departure_event, 100)

    # Add decision variable for choice of activity, guards 1 episode each
    choice_var = problem.add_decision_variable('Choice_'+meal+"-"+date.strftime('%m/%d'), {})

    # Add decision variable for visit or not, guards 6 episodes, 1 goal group, 1 variable
    visit_var = problem.add_decision_variable('IncludeOrNot_'+meal+"-"+date.strftime('%m/%d'), {"Visit": 0.0, "NotVisit": 0.0})
    visit = visit_var.get_assignment('Visit')
    for obj in [ep1, ep2, ep3, ep4, ep5, ep6, choice_var]:
        obj.add_guard(visit)

    goal_group.selection_variable = choice_var
    goal_group.add_guard(visit)

    # Add restaurant episodes
    for idx in range(num_restaurants):
        i = str(idx)
        restaurant = problem.add_episode(start_event, end_event,
                                         DINING_DURATION, DINING_DURATION, True)
        restaurant.name = names[i]
        location = problem.add_location(names[i], FAKE_LAT, FAKE_LON)
        restaurant.start_location = location
        restaurant.end_location = location
        restaurant.time_windows = get_restaurant_time_windows(meal, date)

        goal_group.add_goal_episode(restaurant)
        assignment = choice_var.add_assignment(names[i], RESTAURANT_UTILITY_SCALING * ratings[i])
        restaurant.add_guard(assignment)

    return goal_group

def add_hotels(info, problem, start, user_start, user_end, dates):
    num_hotels = info['Number']
    info_data = info['Structured Content']
    names = info_data['NAME']
    prices = info_data['price']
    room_types = info_data['room type']
    hours_rules = info_data['house_rules']
    minimum_nights = info_data['minimum nights']
    maximum_occupancy = info_data['maximum occupancy']
    review_rate_number = info_data['review rate number']
    cities = info_data['city']

    # Create a goal group for each night, consisting of all choice of hotels
    goal_groups = []
    for day in range(len(dates)-1):
        date = dates[day]
        goal = add_hotel_goal_group(problem, start, user_start, user_end, date, day,
                                    num_hotels, names, prices, room_types,
                                    hours_rules, minimum_nights, maximum_occupancy,
                                    review_rate_number, cities)
        goal_groups.append(goal)

    return goal_groups

def add_hotel_goal_group(problem, start, user_start, user_end, date, day,
                         num_hotels, names, prices, room_types,
                         house_rules, minimum_nights, maximum_occupancy,
                         review_rate_number, cities):

    # TODO: unclear what is the arrival earliest time and departure latest time
    arrival_event = Event()
    arrival_event.earliest_time = date + timedelta(seconds=HOTEL_CHECKIN_TIME)
    start_event = Event()
    end_event = Event()
    departure_event = Event()
    departure_event.latest_time = date + timedelta(days=1) + timedelta(seconds=HOTEL_CHECKOUT_TIME)

    # Add constraint episodes
    ep1 = problem.add_episode(user_start, arrival_event, 0, None)
    ep2 = problem.add_episode(arrival_event, start_event, 0, None)
    # TODO: Relaxable lb of 24 hours
    #  ep3 = problem.add_episode(start_event, end_event, DAY_DURATION, None)
    #  ep3.lb_relaxable = True
    #  ep3.lb_relax_cost = [0.0, 1.0, 0.0]
    ep3 = problem.add_episode(start_event, end_event, 1, None)
    ep4 = problem.add_episode(end_event, departure_event, 0, None)
    ep5 = problem.add_episode(departure_event, user_end, 0, None)
    ep6 = problem.add_episode(arrival_event, departure_event, 0, None)
    # Checkin and checkout time constraint
    ep7 = problem.add_episode(start, start_event,
                              day * DAY_DURATION + HOTEL_CHECKIN_TIME, None)
    ep8 = problem.add_episode(start, end_event, 0.0,
                              (day+1) * DAY_DURATION + HOTEL_CHECKOUT_TIME)
    #  ep9 = problem.add_episode(start, start_event,
    #                            day * DAY_DURATION + HOTEL_PREFERRED_START_TIME, None)
    #  ep9.lb_relaxable = True
    #  ep9.lb_relax_cost = [0.0, 1.0, 0.0]
    #  ep9.ub_relaxable = True
    #  ep9.ub_relax_cost = [0.0, 1.0, 0.0]

    # Add goal group
    goal_group = problem.add_goal_group("Hotel-"+date.strftime('%m/%d'),
                                        start_event, end_event,
                                        arrival_event, departure_event, 200)

    # Add decision variable for choice of hotel, guards 1 episode each
    choice_var = problem.add_decision_variable('Choice_Hotel-'+date.strftime('%m/%d'), {})

    # Add decision variable for visit or not, guards all episodes, 1 goal group
    # TODO: not sure why choice_var is not guarded in ABP encoding, and it's called Yes No
    visit_var = problem.add_decision_variable('IncludeOrNot_Hotel-'+date.strftime('%m/%d'), {"Visit": HOTEL_VISIT_UTILITY, "NotVisit": 0.0})
    visit = visit_var.get_assignment('Visit')
    #  for obj in [ep1, ep2, ep3, ep4, ep5, ep6, ep7, ep8, ep9]:
    for obj in [ep1, ep2, ep3, ep4, ep5, ep6, ep7, ep8]:
        obj.add_guard(visit)

    goal_group.selection_variable = choice_var
    goal_group.add_guard(visit)

    # Add hotel episodes
    for idx in range(num_hotels):
        i = str(idx)
        hotel = problem.add_episode(start_event, end_event,
                                    HOTEL_BASE_DURATION, None, True)
        hotel.name = names[i]
        location = problem.add_location(names[i], FAKE_LAT, FAKE_LON)
        hotel.start_location = location
        hotel.end_location = location

        goal_group.add_goal_episode(hotel)
        assignment = choice_var.add_assignment(names[i], HOTEL_UTILITY_SCALING * review_rate_number[i])
        hotel.add_guard(assignment)
        # TODO: This is also for hotel only in ABP encoding
        hotel.add_guard(visit)

    return goal_group

def get_datetime_from_string(date_string):
    # "2022-03-16"
    date_format = "%Y-%m-%d"
    return datetime.strptime(date_string, date_format)

def get_activity_time_windows(dates):
    time_windows = []
    for date in dates:
        start_time = date + timedelta(seconds=ACTIVITY_START_TIME)
        end_time = date + timedelta(seconds=ACTIVITY_END_TIME)
        time_windows.append([start_time, end_time])
    return time_windows

def get_restaurant_time_windows(meal, date):
    time_windows = []
    if meal == 'Breakfast':
        start_time = date + timedelta(seconds=BREAKFAST_START_TIME)
        end_time = date + timedelta(seconds=BREAKFAST_END_TIME)
    elif meal == 'Lunch':
        start_time = date + timedelta(seconds=LUNCH_START_TIME)
        end_time = date + timedelta(seconds=LUNCH_END_TIME)
    elif meal == 'Dinner':
        start_time = date + timedelta(seconds=DINNER_START_TIME)
        end_time = date + timedelta(seconds=DINNER_END_TIME)
    time_windows.append([start_time, end_time])
    return time_windows


if __name__ == '__main__':
    data = load_jsonl('converted_data/train_data_list.jsonl')
    for problem_data in data[:1]:
        converted_problem = convert_problem(problem_data)
        # Do something with the converted problem
        encoded_problem = json.dumps(converted_problem, cls=CustomEncoder, indent=2)
        print(encoded_problem)

