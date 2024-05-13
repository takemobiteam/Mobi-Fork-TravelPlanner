import json
from definitions import *
from serializer import CustomEncoder

ACTIVITY_DURATION = 60 * 60 # 1 hour
ACTIVITY_UTILITY = 50 # Base utility

def load_jsonl(file_path):
    all_data = []
    with open(file_path, 'r') as f:
        for line in f:
            all_data.append(json.loads(line))
    return all_data

def convert_problem(data):
    start_event = Event()
    end_event = Event()
    problem = Problem(start_event, end_event)

    # Add user_start and end events
    user_start = Event()
    user_end = Event()
    problem.add_episode(start_event, user_start, 0, None)
    problem.add_episode(user_end, end_event, 0, None)

    # Go through each activity in the problem and construct goal groups
    for info in data['structured_ref_info']:
        if info['Info Type'] == 'Attractions':
            add_activities(info, problem, user_start, user_end)

    return problem

def add_activities(info, problem, user_start, user_end):
    num_activities = info['Number']
    info_data = info['Structured Content']
    names = info_data['Name']
    lats = info_data['Latitude']
    lons = info_data['Longitude']
    addresses = info_data['Address']
    phones = info_data['Phone']
    websites = info_data['Website']
    cities = info_data['City']

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
        location = problem.add_location(names[i], lats[i], lons[i])
        activity.start_location = location
        activity.end_location = location
        # TODO: fabricate time windows

        # Add decision variable for choice of activity
        # Guards 1 activity episode
        choice_var = problem.add_decision_variable('Choice_' + names[i],
                                                   {names[i]: ACTIVITY_UTILITY})
        choice = choice_var.get_assignment(names[i])
        activity.add_guard(choice)

        # Add decision variable for visit or not
        # Guards 6 episodes, 1 goal group, 1 variable
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


if __name__ == '__main__':
    data = load_jsonl('converted_data/train_data_list.jsonl')
    for problem_data in data[:1]:
        converted_problem = convert_problem(problem_data)
        # Do something with the converted problem
        encoded_problem = json.dumps(converted_problem, cls=CustomEncoder, indent=2)
        print(encoded_problem)

