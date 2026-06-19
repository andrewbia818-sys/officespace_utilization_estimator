import json
from models.util_data import UtilData
from models.organization import Organization

#a function that generates user-friendly output based on the analysis results, including confidence statements and actionable insights for the client.
def generate_output(organization, sqft_per_employee, estimated_min_sqft_per_employee, estimated_max_sqft_per_employee, confidence_measure_1, confidence_measure_2):
    # print confidence stantment.
    print(f"Based on the analysis, {organization.client_data.organization_name} allocates {sqft_per_employee:.2f} sqft per employee.\n")
    print(f"However, because of systemic absences the effective sqft per employee is between\n")
    print(f"{estimated_min_sqft_per_employee:.2f} and {estimated_max_sqft_per_employee:.2f} sqft. If these figures are above 100 sqft per employee,\n")
    print(f" we can estimate that real estate reduction by a similar factor is achievable using unassigned workspace.\n")
    print(f"Factoring systemic absences there is a {confidence_measure_1} confidence that real estate reduction is \n")
    print(f"achievable, and based on the meeting density there is a {confidence_measure_2} confidence that real \n")
    print(f"estate reduction is achievable.")

#create a json output that includes the key metrics and confidence measures for use in a dashboard or report
    output = {
        "organization_name": organization.client_data.organization_name,
        "sqft_per_employee": sqft_per_employee,
        "estimated_min_sqft_per_employee": estimated_min_sqft_per_employee,
        "estimated_max_sqft_per_employee": estimated_max_sqft_per_employee,
        "confidence_measure_1": confidence_measure_1,
        "confidence_measure_2": confidence_measure_2
    }
    return output
