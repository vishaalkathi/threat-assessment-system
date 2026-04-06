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

    action = decide_action(object_type, threat, speed, distance)

    return {
        "threat": threat,
        "action": action
    }

def decide_action(object_type, threat, speed, distance):

    if object_type == "missile":
        if threat == "CRITICAL":
            return "Deploy flares and perform evasive maneuvers"
        elif threat == "HIGH":
            return "Prepare countermeasures and change trajectory immediately"
        else:
            return "Monitor the situation closely and be ready to take action"
    
    elif object_type == "fighter_jet":
        if threat == "CRITICAL":
            if distance < 30:
                return "Immediate evasive maneuvers and prepare for close combat"
            else:
                return "Engage defensive systems and prepare for potential missile launch"
        elif threat == "HIGH":
            return "Increase distance and prepare for evasive maneuvers"
        else:
            return "Monitor the situation and maintain readiness"
        
    elif object_type == "drone":
        if threat == "CRITICAL":
            return "Attempt signal jamming or deploy counter-drone measures immediately"
        elif threat == "HIGH":
            return "Activate counter-drone measures and maintain vigilance"
        else:
            return "Monitor the situation and be prepared to respond"
    
    else:
        return "Unknown object type, maintain general vigilance and monitor the situation"