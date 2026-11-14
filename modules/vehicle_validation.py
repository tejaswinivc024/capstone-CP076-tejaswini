
import re


def validate_vehicle_number(vehicle_number):
    pattern = r"^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$"

    if re.match(pattern, vehicle_number):
        return True
    else:
        return False
