from pathlib import Path
import joblib
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
BUNDLE = joblib.load(BASE / "models" / "wellness_regression.joblib")
MODEL = BUNDLE["model"]
FEATURES = BUNDLE["features"]

def predict_wellness(values: dict) -> float:
    row = pd.DataFrame([{f: float(values[f]) for f in FEATURES}])
    return float(MODEL.predict(row)[0])
