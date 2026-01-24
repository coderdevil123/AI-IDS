# app/core/config.py

import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

def load_yaml(file_path: Path) -> dict:
    if not file_path.exists():
        raise FileNotFoundError(f"Config file not found: {file_path}")
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

# Load configs
MODEL_CONFIG = load_yaml(BASE_DIR / "configs/model.yaml")
THRESHOLD_CONFIG = load_yaml(BASE_DIR / "configs/thresholds.yaml")
