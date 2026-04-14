from backend.validator import validate_input
from backend.threat_mapping import get_threat_info

from ml.predict import predict_object
from rag.main import get_context
from llm.generate_report import generate_report


def analyze_threat(data):
    valid, message = validate_input(data)
    if not valid:
        return {"error": message}

    ml_output = predict_object(data)

    object_type = ml_output.get("object_type", "unknown")
    confidence = ml_output.get("confidence", 0.0)

    threat_info = get_threat_info(object_type, confidence, data)

    context = get_context(
        object_type,
        data["speed"],
        data["altitude"],
        data["distance"]
    )

    reasoning = []

    speed = data["speed"]
    distance = data["distance"]
    altitude = data["altitude"]
    direction = data["direction"]

    if speed > 1500:
        reasoning.append("High speed detected")

    if distance < 50:
        reasoning.append("Object is very close")

    if altitude < 3000:
        reasoning.append("Low altitude increases potential threat")

    if confidence < 0.6:
        reasoning.append("Low confidence prediction — uncertainty exists")

    if object_type == "missile":
        reasoning.append("Missiles are high-risk threats")

    elif object_type == "fighter_jet":
        reasoning.append("Fighter jets may indicate offensive intent")

    elif object_type == "drone":
        reasoning.append("Drones are usually low-risk unless very close")

    if direction == "approaching":
        reasoning.append("Object is moving towards target")

    elif direction == "leaving":
        reasoning.append("Object is moving away from target")

    if not reasoning:
        reasoning.append("No strong threat indicators detected")

    report = generate_report(
        data,
        ml_output,
        threat_info,
        context,
        reasoning
    )

    return {
        "object_type": object_type,
        "confidence": round(confidence, 2),
        "threat_level": threat_info["threat"],
        "recommended_action": threat_info["action"],
        "reasoning": reasoning,
        "report": report
    }