
from models.organization import Organization
from models.client_data import ClientData
from models.proxy_data import ProxyData
from models.util_data import UtilData

#A function that takes the parsed JSON data after it has been
#validated and creates and Organization object with the client 
# data

def create_organization(data):
    client_data = ClientData(
        organization_name=data["organization_name"],
        employees=data["employees"],
        sqft=data["sqft"],
        vacation_days=data["vacation_days"],
        sick_days=data["sick_days"],
        travel_percentage=data["travel_percentage"],
        vpn_usage_percentage=data["vpn_usage_percentage"],
        peak_login_percentage=data["peak_login_percentage"],
        meeting_hours=data["meeting_hours"],
        hybrid_days=data["hybrid_days"]
    )

    # For now, we'll create a dummy ProxyData object with default values
    proxy_data = ProxyData(
        baseline_working=0,
        in_office_max=0,
        in_office_min=0,
        meeting_density=0,
        peak_login_percentage=0,
        vpn_usage_percentage=0
    )
    # and dummy UtilData object with default values
    util_data = UtilData(
        sqft_per_employee=0,
        estimated_min_sqft_per_employee=0,
        estimated_max_sqft_per_employee=0,
        confidence_measure_1=0,
        confidence_measure_2=0
    )

    organization = Organization(client_data, proxy_data, util_data)
    return organization