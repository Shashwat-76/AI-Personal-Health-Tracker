import pandas as pd

def add_periods(df):
    out = df.copy()
    out["date"] = pd.to_datetime(out["date"])
    out["week"] = out["date"].dt.to_period("W").astype(str)
    out["month"] = out["date"].dt.to_period("M").astype(str)
    return out

def weekly_summary(df):
    x = add_periods(df)
    return x.groupby("week", as_index=False).agg(
        wellness_score=("wellness_score", "mean"),
        sleep_hours=("sleep_hours", "mean"),
        steps=("steps", "mean"),
        exercise_minutes=("exercise_minutes", "mean"),
        stress_level=("stress_level", "mean")
    )

def monthly_summary(df):
    x = add_periods(df)
    return x.groupby("month", as_index=False).agg(
        wellness_score=("wellness_score", "mean"),
        sleep_hours=("sleep_hours", "mean"),
        steps=("steps", "mean"),
        exercise_minutes=("exercise_minutes", "mean"),
        stress_level=("stress_level", "mean")
    )
