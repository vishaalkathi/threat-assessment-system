from rag.build_db import build_db
from rag.query import create_query
from rag.retriever import retrieve

index, data = build_db()

def get_context(obj_type, speed, altitude, distance):
    query = create_query(obj_type, speed, altitude, distance)
    results = retrieve(query, index, data, top_k=4)

    behavior = []
    threat = []
    action = []

    for item in results:
        clean = item.split("] ", 1)[1] if "] " in item else item

        if item.startswith("[BEHAVIOR]"):
            behavior.append(clean)
        elif item.startswith("[THREAT]"):
            threat.append(clean)
        elif item.startswith("[ACTION]"):
            action.append(clean)

    return {
        "behavior": behavior,
        "threat_info": threat,
        "action_info": action
    }