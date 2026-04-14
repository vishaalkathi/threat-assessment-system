from ollama import chat

def generate_report(data, ml_output, threat_info, context, reasoning):

    object_type = ml_output["object_type"]
    confidence = ml_output["confidence"]
    threat = threat_info["threat"]
    action = threat_info["action"]

    behavior = context.get("behavior", [])
    threat_ctx = context.get("threat_info", [])

    prompt = f"""
You are an advanced military threat assessment AI.

Analyze the situation and generate a clear, professional intelligence report.

Object Type: {object_type}
Confidence: {confidence}
Threat Level: {threat}
Recommended Action: {action}

Reasoning Signals:
{reasoning}

Contextual Intelligence:
Behavior: {behavior}
Threat Info: {threat_ctx}

Write a concise but professional threat report.
"""

    response = chat(
        model='mistral',
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]