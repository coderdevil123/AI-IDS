# app/core/preprocess.py

import numpy as np
from app.core.features import FEATURE_COLUMNS

def preprocess_input(payload: dict):
    """
    Converts API JSON input → ML-ready numpy array
    """
    feature_vector = []

    for feature in FEATURE_COLUMNS:
        value = payload.get(feature, 0)
        feature_vector.append(float(value))

    return np.array(feature_vector).reshape(1, -1)
