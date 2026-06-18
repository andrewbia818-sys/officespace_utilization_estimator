class ProxyData:
    def __init__(
        self,
        baseline_working: float,
        in_office_max: float,
        in_office_min: float,
        meeting_density: float,
        peak_login_percentage: float,
        vpn_usage_percentage: float
    ):
        self.baseline_working = baseline_working
        self.in_office_max = in_office_max
        self.in_office_min = in_office_min
        self.meeting_density = meeting_density
        self.peak_login_percentage = peak_login_percentage
        self.vpn_usage_percentage = vpn_usage_percentage
