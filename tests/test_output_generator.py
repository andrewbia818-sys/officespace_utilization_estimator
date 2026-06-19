#test output_generator function
from functions.parser import parse_json_file
from functions.validator import validate_data
from functions.create_org import create_organization
from functions.proxy_calculator import calculate_proxy_features
from functions.analysis_engine import analyze_proxy_features
from functions.output_generator import generate_output
from models.organization import Organization

def test_generate_output():
    data = parse_json_file("data/sample_client.json")
    validate_data(data)
    organization = create_organization(data)
    calculate_proxy_features(organization)
    analyze_proxy_features(organization)
    output = generate_output(
        organization, 
        organization.util_data.sqft_per_employee, 
        organization.util_data.estimated_min_sqft_per_employee, 
        organization.util_data.estimated_max_sqft_per_employee, 
        organization.util_data.confidence_measure_1, 
        organization.util_data.confidence_measure_2
    )
    assert "Based on the analysis" in output
    assert "allocates" in output
    assert "sqft per employee" in output
    assert "effective sqft per employee" in output