from flask import Blueprint, request, jsonify
from app.core.preprocess import preprocess_input

predict_bp = Blueprint("predict", __name__)

@predict_bp.route("/predict", methods=["POST"])
def predict():
    data = request.json

    features = preprocess_input(data.get("features", {}))

    # TEMPORARY stub (real ML comes next step)
    return jsonify({
        "intrusion": False,
        "confidence": 0.0,
        "severity": "LOW"
    })
