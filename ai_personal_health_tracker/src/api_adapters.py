"""
Optional integration interfaces.

Real Fitbit / Apple Health integrations require the user's own export files,
OAuth credentials, permissions, and platform-specific APIs. This project keeps
the ML pipeline provider-agnostic: any adapter only needs to return a DataFrame
with the feature columns expected by the model.
"""

import pandas as pd

REQUIRED_COLUMNS = [
    "date", "sleep_hours", "steps", "exercise_minutes", "water_liters",
    "calories", "protein_g", "stress_level", "resting_heart_rate", "bmi"
]

def validate_health_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    return df.copy()
