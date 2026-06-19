#a function that parses a json file and returns a dictionary
import json

def parse_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError, Exception) as e:
        print(f"Error: {e}")
    except json.JSONDecodeError as e:
        print(f"Error: The JSON file contains invalid syntax. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
