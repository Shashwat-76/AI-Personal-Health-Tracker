import numpy as np
import pandas as pd
from pathlib import Path

SEED = 42
N_DAYS = 365

def generate_dataset(n_days=N_DAYS, seed=SEED):
    rng = np.random.default_rng(seed)
    dates = pd.date_range(end=pd.Timestamp.today().normalize(), periods=n_days, freq="D")

    sleep = np.clip(rng.normal(7.1, 0.9, n_days), 4.5, 9.5)
    steps = np.clip(rng.normal(7600, 2200, n_days), 1500, 15000).astype(int)
    exercise = np.clip(rng.normal(42, 20, n_days), 0, 120)
    water = np.clip(rng.normal(2.3, 0.55, n_days), 0.8, 4.5)
    calories = np.clip(rng.normal(2150, 350, n_days), 1400, 3200)
    protein = np.clip(rng.normal(95, 25, n_days), 40, 180)
    stress = np.clip(rng.normal(5.2, 2.0, n_days), 1, 10)
    rhr = np.clip(rng.normal(69, 7, n_days), 50, 95)
    bmi = np.clip(rng.normal(23.5, 3.0, n_days), 17, 35)

    sleep_quality = np.clip(100 - abs(sleep - 8) * 20, 0, 100)
    activity_score = np.clip(steps / 100, 0, 100) * 0.7 + np.clip(exercise / 1.2, 0, 100) * 0.3
    hydration_score = np.clip(water / 3 * 100, 0, 100)
    stress_score = 100 - stress * 8
    heart_score = 100 - abs(rhr - 60) * 2.5
    bmi_score = 100 - abs(bmi - 21.7) * 7

    wellness = (
        0.25 * sleep_quality +
        0.20 * activity_score +
        0.12 * hydration_score +
        0.15 * stress_score +
        0.15 * heart_score +
        0.08 * bmi_score +
        0.05 * np.clip(protein / 120 * 100, 0, 100)
        + rng.normal(0, 3, n_days)
    )
    wellness = np.clip(wellness, 0, 100)

    return pd.DataFrame({
        "date": dates,
        "sleep_hours": np.round(sleep, 2),
        "steps": steps,
        "exercise_minutes": np.round(exercise, 1),
        "water_liters": np.round(water, 2),
        "calories": np.round(calories).astype(int),
        "protein_g": np.round(protein, 1),
        "stress_level": np.round(stress, 1),
        "resting_heart_rate": np.round(rhr, 1),
        "bmi": np.round(bmi, 1),
        "wellness_score": np.round(wellness, 2)
    })

if __name__ == "__main__":
    out = Path(__file__).resolve().parents[1] / "data" / "health_data.csv"
    out.parent.mkdir(exist_ok=True)
    generate_dataset().to_csv(out, index=False)
    print(f"Saved {len(generate_dataset())} rows to {out}")
