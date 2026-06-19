# Test parser function
from functions.parser import parse_json_file


def test_parse_json_file():
    data = parse_json_file("data/sample_client.json")
    assert data is not None
    assert data["organization_name"] == "Dewey Cheatem & Howe LLP"
    assert data["employees"] == 960
    assert data["sqft"] == 120000