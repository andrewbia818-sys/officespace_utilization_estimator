from models.organization import Organization

#A function that takes an Organization object with the proxy features
# calculated and analyzes them to estimate utilization and occupancy
# metrics with confidence levels.

def analyze_proxy_features(organization):
    # Calculate sqft per emploeee based on the client's current office space and number of employees
    sqft_per_employee = round(organization.client_data.sqft / organization.client_data.employees, 2)
    #print(f"Current sqft per employee: {sqft_per_employee}")
    organization.util_data.sqft_per_employee = sqft_per_employee
    
    # Calculate estimated effective minimum sqft per employee = sqft_per_employee / max_in-office percentage  
    estimated_min_sqft_per_employee = round(sqft_per_employee / (organization.proxy_data.in_office_max/100), 2)
    print(f"Estimated effective minimum sqft per employee: {estimated_min_sqft_per_employee}")
    organization.util_data.estimated_min_sqft_per_employee = estimated_min_sqft_per_employee

     # Calculate estimated effective maximum sqft per employee = sqft_per_employee / min_in-office percentage  
    estimated_max_sqft_per_employee = round(sqft_per_employee / (organization.proxy_data.in_office_min/100), 2)
    #print(f"Estimated effective maximum sqft per employee: {estimated_max_sqft_per_employee}")
    organization.util_data.estimated_max_sqft_per_employee = estimated_max_sqft_per_employee

    # Assess confidence levels based on the proxy features.
    # confidence level 1 - baseline working percentage below 70%
    #  and peak login percentage below baseline_working_percentage 
    # - high confidence that real estate reduction is achievable.
    in_office_average = (organization.proxy_data.in_office_max + organization.proxy_data.in_office_min) / 2
    if in_office_average <  60 and organization.proxy_data.peak_login_percentage < organization.proxy_data.in_office_max:
        confidence_measure_1 = "High"
    elif in_office_average <  70 and organization.proxy_data.peak_login_percentage < organization.proxy_data.in_office_max:
        confidence_measure_1 = "Medium"
    else: 
        confidence_measure_1 = "Low"
    #print(f"Confidence measure 1: {confidence_masure_1}")
    organization.util_data.confidence_measure_1 = confidence_measure_1
    # Confidence level 2 - if meeting_density is above 0.3 and confidence level 1 is high
    # then we have a high confidence that real estate reduction is achievable.
    if organization.proxy_data.meeting_density > 30 and confidence_measure_1 == "High":
        confidence_measure_2 = "High"
    elif organization.proxy_data.meeting_density > 30 and confidence_measure_1 == "Medium":
        confidence_measure_2 = "Medium"
    else:
        confidence_measure_2 = "Low"
    #print(f"Confidence measure 2: {confidence_measure_2}")   
    organization.util_data.confidence_measure_2 = confidence_measure_2
    # print confidence stantment.
    #print(f"Based on the analysis, {organization.client_data.organization_name} allocates {sqft_per_employee:.2f} sqft per employee.\n")
    #print(f"However, because of systemic absences the effective sqft per employee is between\n")
    #print(f"{estimated_min_sqft_per_employee:.2f} and {estimated_max_sqft_per_employee:.2f} sqft. If these figures are above 100 sqft per employee,\n")
    #print(f" we can estimate that real estate reduction by a similar factor is achievable using unassigned workspace.\n")
    #print(f"Factoring systemic absences there is a {confidence_measure_1} confidence that real estate reduction is \n")
    #print(f"achievable, and based on the meeting density there is a {confidence_measure_2} confidence that real \n")
    #print(f"estate reduction is achievable.")

    pass