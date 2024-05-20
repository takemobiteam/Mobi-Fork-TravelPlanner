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
# - Multi-destination attractions and restaurants - how to limit to the city? Does provide lat lons work

EXECUTABLE = "/Users/yuening/mobi/planner/target/planner-0.1-SNAPSHOT-jar-with-dependencies.jar"
PLANNING_VERBOSE = False

def load_jsonl(file_path):
    all_data = []
    with open(file_path, 'r') as f:
        for line in f:
            all_data.append(json.loads(line))
    return all_data

if __name__ == "__main__":
    data = load_jsonl('converted_data/train_data_list.jsonl')
    #  for problem_data in data[:1]:
    #  for problem_data in data[6:7]:
    #  for problem_data in data[1:2]:
    #  for problem_data in data[18:19]:
    for problem_data in data[9:10]:
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
            print(parse_travel_plan(output_filepath, problem_data))
        else:
            print("No solution found")

        print("====================================================")

