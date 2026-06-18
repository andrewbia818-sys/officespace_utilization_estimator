#Step 1 - import json file, call parser function, and print the result
from functions.parser import parse_json_file

data = parse_json_file("data/sample_client.json")
print(data)