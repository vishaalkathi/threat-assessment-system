def get_threat_info(object_type, confidence, data):
    speed = data["speed"]
    distance = data["distance"]

    base_threat = {
        "missile": 3,
        "fighter_jet": 2,
        "drone": 1
    }

    threat_level = base_threat.get(object_type, 1)

    if distance < 50:
        threat_level += 1
    elif distance > 150:
        threat_level -= 1

    if speed > 1500:
        threat_level += 1
    elif speed < 500:
        threat_level -= 1
    
    if confidence < 0.6:
        threat_level -= 1
    
    threat_level = max(0, min(threat_level, 3))

    threat_levels = {
        0: "LOW",
        1: "MEDIUM",
        2: "HIGH",
        3: "CRITICAL"
    }

    threat = threat_levels[threat_level]

    action_map = {
        "LOW": "Monitor situation",
        "MEDIUM": "Prepare defensive action",
        "HIGH": "Evade Immediately",
        "CRITICAL": "Deploy countermeasures immediately"
    }

    action = action_map[threat]

    return {
        "threat": threat,
        "action": action
    }