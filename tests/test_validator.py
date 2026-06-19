#test validator function
from functions.parser import parse_json_file
from functions.validator import validate_data

def test_validate_data():
    data = parse_json_file("data/sample_client.json")
    validate_data(data)
    assert data["organization_name"] == "Dewey Cheatem & Howe LLP"
    assert data["employees"] == 960
    assert data["sqft"] == 120000