def validate_input(data):
    required = ["speed", "altitude", "direction", "distance"]

    for field in required:
        if field not in data:
            return False, f"Missing required field: {field}"
        
    if data["speed"] < 0 or data["altitude"] < 0 or data["distance"] < 0:
        return False, "Speed, altitude, and distance must be non-negative"
    
    return True, "Input is valid"