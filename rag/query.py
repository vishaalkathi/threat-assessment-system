def create_query(obj_type, speed, altitude, distance):
    tags = [obj_type]

    # Speed interpretation
    if speed >= 2000:
        tags.append("extreme speed")
        tags.append("missile-like")
    elif speed >= 800:
        tags.append("high speed")
        tags.append("controlled flight")
    else:
        tags.append("low speed")

    # Altitude interpretation
    if altitude <= 3000:
        tags.append("low altitude")
    else:
        tags.append("high altitude")

    # Distance interpretation
    if distance <= 10:
        tags.append("close range")
        tags.append("high urgency")
    else:
        tags.append("long range")

    # Object-specific semantic hints
    if obj_type.lower() == "missile":
        tags.append("approaching target")
        tags.append("hostile threat")
    elif obj_type.lower() == "drone":
        tags.append("hovering or loitering")
        tags.append("surveillance risk")
    elif obj_type.lower() == "fighter jet":
        tags.append("fast controlled aircraft")
        tags.append("defended airspace")
    elif obj_type.lower() == "debris":
        tags.append("uncontrolled falling object")
        tags.append("non-powered descent")
    else:
        tags.append("unknown aerial object")
        tags.append("requires classification")

    # Retrieval domains
    tags.extend(["behavior", "threat", "action"])

    return " ".join(tags)