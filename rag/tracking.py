def get_movement_status(obj_type, speed, altitude, distance):
    obj = obj_type.lower()

    if obj == "missile":
        if speed >= 2000 and distance <= 10:
            return "Rapidly approaching"
        elif speed >= 2000:
            return "High-speed inbound"
        else:
            return "Approaching"
    elif obj == "drone":
        if altitude <= 1000 and speed <= 300:
            return "Low-altitude localized movement"
        else:
            return "Slow controlled movement"
    elif obj == "fighter jet":
        if speed >= 800:
            return "Fast controlled flight"
        else:
            return "Controlled air movement"
    elif obj == "debris":
        return "Uncontrolled descent"
    else:
        return "Movement pattern uncertain"


def estimate_possible_origin(obj_type, speed, distance):
    obj = obj_type.lower()

    if obj == "missile":
        if distance <= 10:
            return "Likely launched from a nearby hostile zone or mobile platform"
        else:
            return "Possible launch from a distant hostile zone"
    elif obj == "drone":
        return "Possible origin from a nearby local launch point"
    elif obj == "fighter jet":
        return "Likely originating from controlled or contested airspace"
    elif obj == "debris":
        return "Likely residual airborne or spaceborne debris path"
    else:
        return "Origin cannot be determined from current inputs"


def get_priority(threat_level, distance):
    if threat_level == "CRITICAL" and distance <= 10:
        return "Priority 1"
    elif threat_level == "HIGH":
        return "Priority 2"
    elif threat_level == "MEDIUM":
        return "Priority 3"
    else:
        return "Priority 4"