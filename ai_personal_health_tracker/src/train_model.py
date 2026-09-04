from pathlib import Path
import json
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

FEATURES = [
    "sleep_hours", "steps", "exercise_minutes", "water_liters",
    "calories", "protein_g", "stress_level", "resting_heart_rate", "bmi"
]
TARGET = "wellness_score"

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data" / "health_data.csv"
MODEL_DIR = BASE / "models"

df = pd.read_csv(DATA, parse_dates=["date"]).dropna()
X = df[FEATURES]
y = df[TARGET]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=250, max_depth=10, min_samples_leaf=2, random_state=42
)
model.fit(X_train, y_train)
pred = model.predict(X_test)

metrics = {
    "MAE": round(mean_absolute_error(y_test, pred), 3),
    "RMSE": round(mean_squared_error(y_test, pred) ** 0.5, 3),
    "R2": round(r2_score(y_test, pred), 3)
}

MODEL_DIR.mkdir(exist_ok=True)
joblib.dump({"model": model, "features": FEATURES}, MODEL_DIR / "wellness_regression.joblib")
(MODEL_DIR / "metrics.json").write_text(json.dumps(metrics, indent=2))

print("Model saved.")
print(metrics)
