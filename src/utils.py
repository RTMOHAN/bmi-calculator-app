def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_valid_weight(weight):
    return is_numeric(weight) and 30 <= float(weight) <= 500

def is_valid_height(height):
    return is_numeric(height) and 0.5 <= float(height) <= 3.0  # Height in meters

def validate_inputs(weight, height):
    if not is_valid_weight(weight):
        return "Weight must be a number between 30 and 500 kg."
    if not is_valid_height(height):
        return "Height must be a number between 0.5 and 3.0 meters."
    return None  # Inputs are valid