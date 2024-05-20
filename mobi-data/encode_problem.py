from params import *
from definitions import *
from datetime import datetime, timedelta

def encode_problem(data):
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

    # Create budget constraint if exists
    if 'budget' in data:
        budget = SumConstraint()
        budget.name = 'Budget'
        budget.upperbound = data['budget']
        budget.ub_relaxation_cost = [0.0, 1.0e20]
        # TODO: add budget constraint back
        #  problem.add_global_constraint(budget)
    else:
        budget = None

    # Go through each activity in the problem and construct goal groups
    idx_hotel = 0
    for info in data['structured_ref_info']:
        if info['Info Type'] == 'Attractions':
            goal_groups = add_activities(info, problem, user_start, user_end, dates)
            for goal_group in goal_groups:
                agent.add_goal_group(goal_group)
        elif info['Info Type'] == 'Restaurants':
            goal_groups = add_restaurants(info, problem, user_start, user_end, dates, budget)
            for goal_group in goal_groups:
                agent.add_goal_group(goal_group)
        elif info['Info Type'] == 'Accommodations':
            goal_groups = add_hotels(info, problem, start_event, user_start, user_end, dates, budget, idx_hotel)
            for goal_group in goal_groups:
                agent.add_goal_group(goal_group)
            idx_hotel += 2

    # Add transportation
    goal_groups = add_transportation(data, problem, user_start, user_end, dates)
    for goal_group in goal_groups:
        agent.add_goal_group(goal_group)

    return problem


# #######################################
# Function to add attractions to problem
# #######################################
def add_activities(info, problem, user_start, user_end, dates):
    num_activities = info['Number']
    if num_activities < 1:
        return []
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


# #######################################
# Function to add restaurants to problem
# #######################################
def add_restaurants(info, problem, user_start, user_end, dates, budget):
    num_restaurants = info['Number']
    if num_restaurants < 1:
        return []
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
                                             ratings, cities, budget)
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
                              ratings, cities, budget):
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
        if budget:
            budget.set_episode_value(restaurant, costs[i])

    return goal_group


# #######################################
# Function to add hotels to problem
# #######################################
def add_hotels(info, problem, start, user_start, user_end, dates, budget, idx_hotel):
    num_hotels = info['Number']
    if num_hotels < 1:
        return []
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
    #  for day in range(len(dates)-1):
    for day in [idx_hotel, idx_hotel+1]:
        date = dates[day]
        goal = add_hotel_goal_group(problem, start, user_start, user_end, date, day,
                                    num_hotels, names, prices, room_types,
                                    hours_rules, minimum_nights, maximum_occupancy,
                                    review_rate_number, cities, budget)
        goal_groups.append(goal)

    return goal_groups

def add_hotel_goal_group(problem, start, user_start, user_end, date, day,
                         num_hotels, names, prices, room_types,
                         house_rules, minimum_nights, maximum_occupancy,
                         review_rate_number, cities, budget):

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
        if budget:
            budget.set_episode_value(hotel, prices[i])

    return goal_group


# #######################################
# Function to add transportation to problem
# #######################################
def add_transportation(data, problem, user_start, user_end, dates, budget=None):
    date2info = {}
    # TODO: Hack to get the date for driving options
    i_driving = 0
    i_taxi = 0
    for info in data['structured_ref_info']:
        if info['Info Type'] == 'Flight':
            populate_flight_info(info, date2info)
        elif info['Info Type'] == 'Self-driving':
            i_driving = populate_driving_info(info, date2info, dates, i_driving, 'self-driving')
        elif info['Info Type'] == 'Taxi':
            i_taxi = populate_driving_info(info, date2info, dates, i_taxi, 'taxi')

    goal_groups = []
    i = 0
    while i < len(dates):
        date = dates[i].strftime('%Y-%m-%d')
        # TODO: hardcoded for travel planning problem
        i += 2
        info = date2info[date] if date in date2info else []
        date = get_datetime_from_string(date)

        # Create a goal group for the different flight
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

        # Flight is a must visit, create a choice var
        choice_var = problem.add_decision_variable('Choice_Flight-'+date.strftime('%m/%d'), {})

        # Add goal group
        goal_group = problem.add_goal_group("Flight-"+date.strftime('%m/%d'),
                                            start_event, end_event,
                                            arrival_event, departure_event, 300)
        goal_group.selection_variable = choice_var

        # Create a dummy flight that is infeasible -- fail when no flight options
        # Such a flight has no time window or arrival/departure time, hence no availablity
        dummy_flight = problem.add_episode(start_event, end_event,
                                           0, None, True)
        dummy_flight.name = 'No Flight'
        dummy_flight.start_location = problem.add_location("DUMMY",
                                                           FAKE_LAT, FAKE_LON)
        dummy_flight.end_location = problem.add_location("DUMMY",
                                                         FAKE_LAT, FAKE_LON)
        goal_group.add_goal_episode(dummy_flight)
        assignment = choice_var.add_assignment('No Flight', 0.0)
        dummy_flight.add_guard(assignment)

        for flight_info in info:
            # Add flight episode
            flight = problem.add_episode(start_event, end_event,
                                         flight_info['duration'],
                                         flight_info['duration'], True)
            flight.name = flight_info['type'] + flight_info['name']
            flight.start_location = problem.add_location(flight_info['origin_city'],
                                                         FAKE_LAT, FAKE_LON)
            flight.end_location = problem.add_location(flight_info['dest_city'],
                                                       FAKE_LAT, FAKE_LON)
            # TODO: flight time should be improved, try scheduled time?
            # Right now, this is proving a buffer so that its availability is non-zero
            flight.time_windows = [[flight_info['start_time'] - timedelta(seconds=FLIGHT_BUFFER_TIME),
                                    flight_info['end_time'] + timedelta(seconds=FLIGHT_BUFFER_TIME)]]

            goal_group.add_goal_episode(flight)
            assignment = choice_var.add_assignment(flight.name,
                                                   FLIGHT_UTILITY_SCALING * FLIGHT_STANDARD_DURATION/flight_info['duration'])
            flight.add_guard(assignment)
            if budget:
                budget.set_episode_value(flight, flight_info['price'])

        goal_groups.append(goal_group)

    return goal_groups


def populate_flight_info(info, date2info):
    num_flights = info['Number']
    if num_flights < 1:
        return
    info_data = info['Structured Content']
    flight_numbers = info_data['Flight Number']
    origin_cities = info_data['OriginCityName']
    dest_cities = info_data['DestCityName']
    # Time in the form of "hh:mm"
    departure_times = info_data['DepTime']
    arrival_times = info_data['ArrTime']
    durations = info_data['ActualElapsedTime']
    flight_dates = info_data['FlightDate']
    prices = info_data['Price']
    distances = info_data['Distance']

    for idx in range(num_flights):
        i = str(idx)
        flight_date = get_datetime_from_string(flight_dates[i])
        start_time = get_time_from_string(departure_times[i])
        end_time = get_time_from_string(arrival_times[i])
        start_datetime = flight_date.replace(hour=start_time.hour,
                                             minute=start_time.minute)
        end_datetime = flight_date.replace(hour=end_time.hour,
                                           minute=end_time.minute)
        # Check if end_time is before start_time and adjust abs_end_time if necessary
        if end_time < start_time:
            end_datetime += timedelta(days=1)
        if flight_date not in date2info:
            date2info[flight_dates[i]] = []
        date2info[flight_dates[i]].append({
            'type': 'flight',
            'name': '-' + flight_numbers[i],
            'origin_city': origin_cities[i],
            'dest_city': dest_cities[i],
            'start_time': start_datetime,
            'end_time': end_datetime,
            'duration': get_duration_from_string(durations[i]),
            'price': prices[i],
            'distance': distances[i]
            })

def populate_driving_info(info, date2info, dates, i, type_name):
    if info['Number'] == 1:
        origin = info['Structured Content']['origin']
        dest = info['Structured Content']['destination']
        duration = info['Structured Content']['duration']
        cost = info['Structured Content']['cost']
        distance = info['Structured Content']['distance']
        date = dates[i].strftime('%Y-%m-%d')

        date2info[date] = [{
            'type': type_name,
            'name': '',
            'origin_city': origin,
            'dest_city': dest,
            'duration': get_duration_from_string(duration),
            'price': cost,
            'distance': distance,
            'start_time': get_datetime_from_string(date),
            'end_time': get_datetime_from_string(date) + timedelta(days=1)
        }]

    return i + 2

# #######################################
# Helper functions
# #######################################
def get_duration_from_string(duration_string):
    # "x hours x minutes"
    duration = duration_string.split()
    hours = int(duration[0])
    minutes = int(duration[2])
    return hours * 60 * 60 + minutes * 60

def get_datetime_from_string(date_string):
    # "2022-03-16"
    date_format = "%Y-%m-%d"
    return datetime.strptime(date_string, date_format)

def get_time_from_string(time_string):
    time_format = "%H:%M"
    return datetime.strptime(time_string, time_format).time()

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

