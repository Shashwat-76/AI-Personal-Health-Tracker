from pathlib import Path
import json
import pandas as pd
import plotly.express as px
import streamlit as st

from src.predictor import predict_wellness
from src.trend_analysis import weekly_summary, monthly_summary
from src.health_agent import generate_insights

BASE = Path(__file__).resolve().parent
DATA = BASE / "data" / "health_data.csv"
METRICS = BASE / "models" / "metrics.json"

st.set_page_config(page_title="AI Personal Health Tracker", page_icon="❤️", layout="wide")

st.title("❤️ AI Personal Health Tracker")
st.caption("Machine-learning wellness trend demo • Educational use only, not medical advice")

df = pd.read_csv(DATA, parse_dates=["date"])
metrics = json.loads(METRICS.read_text())

# Sidebar
st.sidebar.header("Today's Inputs")
sleep = st.sidebar.slider("Sleep (hours)", 4.0, 10.0, 7.5, 0.1)
steps = st.sidebar.number_input("Steps", 0, 30000, 8000, 500)
exercise = st.sidebar.number_input("Exercise (minutes)", 0, 240, 45, 5)
water = st.sidebar.slider("Water (liters)", 0.5, 5.0, 2.5, 0.1)
calories = st.sidebar.number_input("Calories", 1000, 5000, 2200, 50)
protein = st.sidebar.number_input("Protein (g)", 20, 300, 100, 5)
stress = st.sidebar.slider("Stress (1 low – 10 high)", 1.0, 10.0, 4.0, 0.5)
rhr = st.sidebar.number_input("Resting heart rate", 40.0, 120.0, 68.0, 1.0)
bmi = st.sidebar.number_input("BMI", 15.0, 45.0, 23.0, 0.1)

current = {
    "sleep_hours": sleep, "steps": steps, "exercise_minutes": exercise,
    "water_liters": water, "calories": calories, "protein_g": protein,
    "stress_level": stress, "resting_heart_rate": rhr, "bmi": bmi
}

score = predict_wellness(current)
score = max(0, min(100, score))

c1, c2, c3, c4 = st.columns(4)
c1.metric("Predicted Wellness", f"{score:.1f}/100")
c2.metric("Avg Sleep", f"{df.sleep_hours.mean():.1f} h")
c3.metric("Avg Steps", f"{df.steps.mean():,.0f}")
c4.metric("Model R²", f"{metrics['R2']:.2f}")

st.subheader("AI Health Insights")
for insight in generate_insights(current, score):
    st.info(insight)

st.subheader("Historical Trends")
tab1, tab2 = st.tabs(["Weekly", "Monthly"])

with tab1:
    weekly = weekly_summary(df)
    fig = px.line(weekly, x="week", y="wellness_score", markers=True,
                  title="Average Weekly Wellness Score")
    fig.update_layout(xaxis_title="Week", yaxis_title="Wellness score")
    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.line(weekly, x="week", y=["sleep_hours", "stress_level"],
                   title="Weekly Sleep and Stress")
    st.plotly_chart(fig2, use_container_width=True)

with tab2:
    monthly = monthly_summary(df)
    fig3 = px.line(monthly, x="month", y="wellness_score", markers=True,
                   title="Average Monthly Wellness Score")
    fig3.update_layout(xaxis_title="Month", yaxis_title="Wellness score")
    st.plotly_chart(fig3, use_container_width=True)

st.subheader("Recent Data")
st.dataframe(df.tail(14).sort_values("date", ascending=False), use_container_width=True)

st.subheader("Model Evaluation")
st.write({
    "MAE": metrics["MAE"],
    "RMSE": metrics["RMSE"],
    "R²": metrics["R2"]
})
st.caption("The included dataset is synthetic and the score is a demonstration target, not a clinical health assessment.")
