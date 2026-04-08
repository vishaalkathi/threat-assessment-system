def create_query(obj_type, speed, altitude, distance):
    tags = [obj_type]

    if speed >= 2000:
        tags.append("high speed")
    elif speed >= 800:
        tags.append("medium speed")
    else:
        tags.append("low speed")

    if altitude <= 3000:
        tags.append("low altitude")
    else:
        tags.append("high altitude")

    if distance <= 50:
        tags.append("close range")
    else:
        tags.append("long range")

    return " ".join(tags)