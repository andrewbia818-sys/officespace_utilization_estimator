from functions.parser import parse_json_file
from models.organization import Organization
from models.client_data import ClientData
from models.proxy_data import ProxyData
from functions.validator import validate_data
from functions.create_org import create_organization
from functions.proxy_calculator import calculate_proxy_features
from pprint import pprint
from functions.analysis_engine import analyze_proxy_features

# Step 1 - import json file, call parser function, and 
# print the result
data = parse_json_file("data/sample_client.json")
print(f"Client data: {data}")

# Step 2 - validate the data and create an Organization object
validate_data(data)
organization = create_organization(data)
pprint(vars(organization.client_data))
pprint(vars(organization.proxy_data))

# Step 3 - calculate proxy features and add them to the 
# Organization object
calculate_proxy_features(organization)
pprint(vars(organization.proxy_data))

#Step 4 - analyze the proxy features to estimate 
# utilization and occupancy with confidence levels
analyze_proxy_features(organization)

# Step 5 - output the results in a user-friendly format

# Step 6 - Use industry benchmarks to estimate the office space 
# needs of the client based on the estimated utilization and 
# occupancy metrics and estimate annual $ savings 
# from space reduction.