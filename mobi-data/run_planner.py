import json
from definitions import *
from params import *
from parse_solution import parse_travel_plan
from encode_problem import encode_problem
from serializer import CustomEncoder
import subprocess
import os

# TODOs:
# - Provide lat lons to locations in different cities
# - Add budget constraint back
# - Fill in complete plan output information
# - Pre-filter POI based on constraints?
# - Multi-destination attractions and restaurants - how to limit to the city? Does provide lat lons work?
#     - Limit using time windows to specific days -- solution still cross over a bit day boundaries. Is it because timezone?
# - Problem with using lat lon -- planner cannot insert a first flight activity due to it taking an extreme amount of time, needs round trip, does planner web interface determine the flight already?

EXECUTABLE = "/Users/yuening/mobi/planner/target/planner-0.1-SNAPSHOT-jar-with-dependencies.jar"
EXECUTABLE = "/Users/jiahaoliu/src/planner/target/planner-0.1-SNAPSHOT-jar-with-dependencies.jar"
PLANNING_VERBOSE = False

def load_jsonl(file_path):
    all_data = []
    with open(file_path, 'r') as f:
        for line in f:
            all_data.append(json.loads(line))
    return all_data

def run_tests(validation=False, solution_filepath=None):
    if validation:
        data = load_jsonl('converted_data/val_data_list.jsonl')
    else:
        data = load_jsonl('converted_data/train_data_list.jsonl')

    if solution_filepath is not None:
        if os.path.exists(solution_filepath):
            os.remove(solution_filepath)

    for problem_data in data:
        print("# Problem %d" % problem_data['original_data_index'])

        problem = encode_problem(problem_data)
        problem_json = json.dumps(problem, cls=CustomEncoder, indent=2)

        input_filepath = "tempPlanning.problem"
        output_filepath = "tempPlanningABP.solution"
        with open(input_filepath, 'w') as f:
            f.write(problem_json)

        # Run the planner and record the solution
        if os.path.exists(output_filepath):
            os.remove(output_filepath)
        # Do not output subprocess output if PLANNING_VERBOSE is False
        if PLANNING_VERBOSE:
            subprocess.run(["java", "-jar", EXECUTABLE, input_filepath, output_filepath])
        else:
            subprocess.run(["java", "-jar", EXECUTABLE, input_filepath, output_filepath], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if os.path.exists(output_filepath):
            plan = parse_travel_plan(output_filepath, problem_data)
            print(plan)
        else:
            plan = None
            print("No solution found")
        res = {
                "idx": problem_data['original_data_index'],
                "query": problem_data['query'],
                "plan": plan
                }
        if solution_filepath is not None:
            with open(solution_filepath, 'a') as f:
                f.write(json.dumps(res) + '\n')

        print("====================================================")


if __name__ == "__main__":
    run_tests(validation=False, solution_filepath='train_solution.jsonl')
    #  run_tests(validation=True, solution_filepath='val_solution.jsonl')
