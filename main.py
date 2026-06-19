import json

from functions.parser import parse_json_file
from models.organization import Organization
from models.client_data import ClientData
from models.proxy_data import ProxyData
from functions.validator import validate_data
from functions.create_org import create_organization
from functions.proxy_calculator import calculate_proxy_features
from pprint import pprint
from functions.analysis_engine import analyze_proxy_features
from functions.output_generator import generate_output

# Step 1 - import json file, call parser function, and 
# print the result
data = parse_json_file("data/sample_client.json")
#print(f"Client data: {data}")

# Step 2 - validate the data and create an Organization object
validate_data(data)
organization = create_organization(data)
pprint(vars(organization.client_data))
#pprint(vars(organization.proxy_data))

# Step 3 - calculate proxy features and add them to the 
# Organization object
calculate_proxy_features(organization)
pprint(vars(organization.proxy_data))

#Step 4 - analyze the proxy features to estimate 
# utilization and occupancy with confidence levels
analyze_proxy_features(organization)
#pprint(vars(organization.util_data))

# Step 5 - output the results in a user-friendly format
output = generate_output(
    organization, 
    organization.util_data.sqft_per_employee, 
    organization.util_data.estimated_min_sqft_per_employee, 
    organization.util_data.estimated_max_sqft_per_employee, 
    organization.util_data.confidence_measure_1, 
    organization.util_data.confidence_measure_2
)
print(json.dumps(output, indent=2))
# Step 6 - Use industry benchmarks to estimate the office space reduction potential and provide actionable insights for the client. (This step is not implemented in this code snippet but can be added in the future by creating a function that takes the analysis results and compares them to industry benchmarks to provide recommendations for real estate reduction strategies.)
