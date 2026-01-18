# app/core/thresholds.py

def severity_from_confidence(confidence: float):
    if confidence >= 0.9:
        return "CRITICAL"
    elif confidence >= 0.75:
        return "HIGH"
    elif confidence >= 0.5:
        return "MEDIUM"
    else:
        return "LOW"
