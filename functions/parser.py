#a function that parses a json file and returns a dictionary
import json
def parse_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data