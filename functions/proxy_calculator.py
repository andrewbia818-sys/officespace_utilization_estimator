from models.organization import Organization

#A function that takes an Organization object and calculates 
# the proxy features
def calculate_proxy_features(organization: Organization):

    baseline_working = 100 * (1 - (organization.client_data.vacation_days + organization.client_data.sick_days) / 260)  # Assuming 260 working days in a year
    organization.proxy_data.baseline_working = baseline_working

    in_office_max = baseline_working - organization.client_data.travel_percentage
    organization.proxy_data.in_office_max = in_office_max

    in_office_min = in_office_max - 100 * (organization.client_data.hybrid_days/5)   
    organization.proxy_data.in_office_min = in_office_min

    meeting_density = organization.client_data.meeting_hours / 8 # 8 hours per day
    if meeting_density > 1:
        meeting_density = 1
    organization.proxy_data.meeting_density = meeting_density

    organization.proxy_data.peak_login_percentage = organization.client_data.peak_login_percentage

    organization.proxy_data.vpn_usage_percentage = organization.client_data.vpn_usage_percentage
