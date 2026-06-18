from models.client_data import ClientData
from models.proxy_data import ProxyData

class Organization:
    """
    Object represents a client organization.
    Holds raw client data, calculated proxy features,
    and estimated utilization and occupancy metrics.
    """

    def __init__(self, client_data: ClientData, proxy_data: ProxyData):
        self.client_data = client_data
        self.proxy_data = proxy_data