class UtilData:
    def __init__(
        self,
        sqft_per_employee: float,
        estimated_min_sqft_per_employee: float,
        estimated_max_sqft_per_employee: float,
        confidence_measure_1: str,
        confidence_measure_2: str
    ):
        self.sqft_per_employee = sqft_per_employee
        self.estimated_min_sqft_per_employee = estimated_min_sqft_per_employee
        self.estimated_max_sqft_per_employee = estimated_max_sqft_per_employee
        self.confidence_measure_1 = confidence_measure_1
        self.confidence_measure_2 = confidence_measure_2    
