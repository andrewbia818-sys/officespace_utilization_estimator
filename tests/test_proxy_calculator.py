#test proxy_calculator function
from functions.parser import parse_json_file
from functions.validator import validate_data
from functions.create_org import create_organization
from functions.proxy_calculator import calculate_proxy_features
from models.organization import Organization

def test_calculate_proxy_features():
    data = parse_json_file("data/sample_client.json")
    validate_data(data)
    organization = create_organization(data)
    calculate_proxy_features(organization)
    assert organization.proxy_data.vpn_usage_percentage == 35
    assert organization.proxy_data.peak_login_percentage == 55
    assert organization.proxy_data.meeting_hours == 3.5