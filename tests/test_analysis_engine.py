#test analysis_engine function
from functions.parser import parse_json_file
from functions.validator import validate_data
from functions.create_org import create_organization
from functions.proxy_calculator import calculate_proxy_features
from functions.analysis_engine import analyze_proxy_features
from models.organization import Organization

def test_analyze_proxy_features():
    data = parse_json_file("data/sample_client.json")
    validate_data(data)
    organization = create_organization(data)
    calculate_proxy_features(organization)
    analyze_proxy_features(organization)
    assert organization.util_data.sqft_per_employee == 125
    assert organization.util_data.estimated_min_sqft_per_employee == 100
    assert organization.util_data.estimated_max_sqft_per_employee == 150
    assert organization.util_data.confidence_measure_1 == "high"
    assert organization.util_data.confidence_measure_2 == "medium"