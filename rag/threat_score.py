def compute_threat_score(obj_type, speed, altitude, distance):
    score = 0

    obj = obj_type.lower()

    # Object-type contribution
    if obj == "missile":
        score += 40
    elif obj == "fighter jet":
        score += 25
    elif obj == "drone":
        score += 15
    elif obj == "debris":
        score += 5
    else:
        score += 10

    # Speed contribution
    if speed >= 2000:
        score += 30
    elif speed >= 800:
        score += 20
    elif speed >= 200:
        score += 10

    # Altitude contribution
    if altitude <= 3000:
        score += 15
    else:
        score += 5

    # Distance contribution
    if distance <= 10:
        score += 15
    elif distance <= 50:
        score += 10
    else:
        score += 5

    return min(score, 100)


def get_threat_level(score):
    if score >= 80:
        return "CRITICAL"
    elif score >= 60:
        return "HIGH"
    elif score >= 40:
        return "MEDIUM"
    else:
        return "LOW"