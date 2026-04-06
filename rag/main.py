from rag.tracking import get_movement_status, estimate_possible_origin, get_priority
from rag.build_db import build_db
from rag.query import create_query
from rag.retriever import retrieve
from rag.threat_score import compute_threat_score, get_threat_level

index, data = build_db()

def generate_summary(obj_type, speed, altitude, distance, threat_level):
    obj = obj_type.lower()

    if obj == "missile":
        return "High-speed close-range object consistent with missile threat."
    elif obj == "drone":
        return "Low-altitude object showing characteristics consistent with drone activity."
    elif obj == "fighter jet":
        return "High-speed controlled aircraft detected near defended airspace."
    elif obj == "debris":
        return "Object behavior is more consistent with falling debris than controlled flight."
    else:
        return f"Object classified as {obj_type} with threat level {threat_level}."

def generate_urgency(threat_level, distance):
    if threat_level == "CRITICAL" and distance <= 10:
        return "IMMEDIATE"
    elif threat_level in ["CRITICAL", "HIGH"]:
        return "HIGH"
    elif threat_level == "MEDIUM":
        return "MODERATE"
    else:
        return "LOW"

def generate_confidence_note(obj_type, threat_level):
    obj = obj_type.lower()

    if obj == "debris":
        return "Assessment indicates lower likelihood of intentional hostile behavior."
    elif threat_level == "CRITICAL":
        return "Multiple strong indicators support this assessment."
    elif threat_level == "HIGH":
        return "Assessment is supported by several threat-related indicators."
    elif threat_level == "MEDIUM":
        return "Assessment should be monitored as additional data becomes available."
    else:
        return "Current indicators suggest low immediate concern."

def generate_recommendation(threat_level, obj_type):
    if threat_level == "CRITICAL":
        return {
            "primary_action": "Initiate immediate defensive response",
            "secondary_action": "Maintain continuous tracking and prepare countermeasures"
        }
    elif threat_level == "HIGH":
        return {
            "primary_action": "Prioritize tracking and prepare interception",
            "secondary_action": "Reassess continuously as new data arrives"
        }
    elif threat_level == "MEDIUM":
        return {
            "primary_action": "Monitor object closely",
            "secondary_action": "Escalate response if movement becomes more aggressive"
        }
    else:
        return {
            "primary_action": "Continue observation",
            "secondary_action": "No immediate engagement required"
        }

from rag.build_db import build_db
from rag.query import create_query
from rag.retriever import retrieve
from rag.threat_score import compute_threat_score, get_threat_level
from rag.tracking import get_movement_status, estimate_possible_origin, get_priority

index, data = build_db()

def generate_summary(obj_type, speed, altitude, distance, threat_level):
    obj = obj_type.lower()

    if obj == "missile":
        return "High-speed close-range object consistent with missile threat."
    elif obj == "drone":
        return "Low-altitude object showing characteristics consistent with drone activity."
    elif obj == "fighter jet":
        return "High-speed controlled aircraft detected near defended airspace."
    elif obj == "debris":
        return "Object behavior is more consistent with falling debris than controlled flight."
    else:
        return f"Object classified as {obj_type} with threat level {threat_level}."

def generate_urgency(threat_level, distance):
    if threat_level == "CRITICAL" and distance <= 10:
        return "IMMEDIATE"
    elif threat_level in ["CRITICAL", "HIGH"]:
        return "HIGH"
    elif threat_level == "MEDIUM":
        return "MODERATE"
    else:
        return "LOW"

def generate_confidence_note(obj_type, threat_level):
    obj = obj_type.lower()

    if obj == "debris":
        return "Assessment indicates lower likelihood of intentional hostile behavior."
    elif threat_level == "CRITICAL":
        return "Multiple strong indicators support this assessment."
    elif threat_level == "HIGH":
        return "Assessment is supported by several threat-related indicators."
    elif threat_level == "MEDIUM":
        return "Assessment should be monitored as additional data becomes available."
    else:
        return "Current indicators suggest low immediate concern."

def generate_recommendation(threat_level, obj_type):
    if threat_level == "CRITICAL":
        return {
            "primary_action": "Initiate immediate defensive response",
            "secondary_action": "Maintain continuous tracking and prepare countermeasures"
        }
    elif threat_level == "HIGH":
        return {
            "primary_action": "Prioritize tracking and prepare interception",
            "secondary_action": "Reassess continuously as new data arrives"
        }
    elif threat_level == "MEDIUM":
        return {
            "primary_action": "Monitor object closely",
            "secondary_action": "Escalate response if movement becomes more aggressive"
        }
    else:
        return {
            "primary_action": "Continue observation",
            "secondary_action": "No immediate engagement required"
        }

def get_context(obj_type, speed, altitude, distance):
    query = create_query(obj_type, speed, altitude, distance)
    results = retrieve(query, index, data, top_k=4)

    observed_behavior = []
    risk_factors = []
    supporting_actions = []

    for item in results:
        clean_item = item.split("] ", 1)[1] if "] " in item else item

        if item.startswith("[BEHAVIOR]"):
            observed_behavior.append(clean_item)
        elif item.startswith("[THREAT]"):
            risk_factors.append(clean_item)
        elif item.startswith("[ACTION]"):
            supporting_actions.append(clean_item)

    threat_score = compute_threat_score(obj_type, speed, altitude, distance)
    threat_level = get_threat_level(threat_score)
    urgency = generate_urgency(threat_level, distance)

    recommendation = generate_recommendation(threat_level, obj_type)

    movement_status = get_movement_status(obj_type, speed, altitude, distance)
    possible_origin = estimate_possible_origin(obj_type, speed, distance)
    priority = get_priority(threat_level, distance)

    return {
        "object_details": {
            "type": obj_type,
            "speed": speed,
            "altitude": altitude,
            "distance": distance
        },
        "threat_assessment": {
            "score": threat_score,
            "level": threat_level,
            "urgency": urgency,
            "summary": generate_summary(obj_type, speed, altitude, distance, threat_level)
        },
        "analysis": {
            "observed_behavior": observed_behavior,
            "risk_factors": risk_factors,
            "confidence_note": generate_confidence_note(obj_type, threat_level)
        },
        "recommended_response": {
            "primary_action": recommendation["primary_action"],
            "secondary_action": recommendation["secondary_action"],
            "supporting_actions": supporting_actions
        },
        "tracking": {
            "movement_status": movement_status,
            "possible_origin": possible_origin,
            "priority": priority
        }
    }