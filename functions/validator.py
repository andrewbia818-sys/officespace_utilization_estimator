# a function that validates the input data from the JSON file and
#if valid prints "Data is valid", otherwise raises an error with 
# a message indicating the issue

def validate_data(data):
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")

    required_keys = [
        "organization_name",
        "employees",
        "sqft",
        "vacation_days",
        "sick_days",
        "travel_percentage",
        "vpn_usage_percentage",
        "peak_login_percentage",
        "meeting_hours",
        "hybrid_days"
    ]

    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing required key: {key}")

    if not isinstance(data["employees"], int) or data["employees"] <= 0:
        raise ValueError("employees must be a positive integer")

    if not isinstance(data["sqft"], int) or data["sqft"] <= 0:
        raise ValueError("sqft must be a positive integer")

    if not isinstance(data["vacation_days"], (int, float)):
        raise ValueError("vacation_days must be a number")

    if not isinstance(data["sick_days"], (int, float)):
        raise ValueError("sick_days must be a number")

    if not isinstance(data["travel_percentage"], (int, float)):
        raise ValueError("travel_percentage must be a number")

    if not isinstance(data["vpn_usage_percentage"], (int, float)):
        raise ValueError("vpn_usage_percentage must be a number")

    if not isinstance(data["peak_login_percentage"], (int, float)):
        raise ValueError("peak_login_percentage must be a number")

    if not isinstance(data["meeting_hours"], (int, float)):
        raise ValueError("meeting_hours must be a number")

    if not isinstance(data["hybrid_days"], (int, float)):
        raise ValueError("hybrid_days must be a number")

    print("Data is valid")  