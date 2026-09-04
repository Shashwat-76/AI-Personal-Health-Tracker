def generate_insights(row: dict, predicted_score: float) -> list[str]:
    insights = []

    if row["sleep_hours"] < 6.5:
        insights.append("Sleep is below the demo target range; improving sleep consistency may support recovery.")
    elif row["sleep_hours"] >= 7.5:
        insights.append("Sleep duration is in a strong range for this demo model.")

    if row["steps"] < 6000:
        insights.append("Daily activity is relatively low; consider adding light walking or movement breaks.")
    elif row["steps"] >= 9000:
        insights.append("Daily step count is strong in the current input.")

    if row["stress_level"] >= 7:
        insights.append("Stress level is elevated; consider recovery time, relaxation, and workload breaks.")

    if row["water_liters"] < 2:
        insights.append("Hydration is relatively low compared with the demo target.")

    if row["resting_heart_rate"] > 80:
        insights.append("Resting heart rate is relatively high in this input; track the trend rather than a single reading.")

    if predicted_score >= 80:
        insights.append("Overall demo wellness score is strong. Maintaining consistent habits is the key trend.")
    elif predicted_score >= 60:
        insights.append("Overall demo wellness score is moderate. Focus on the weakest contributing habits first.")
    else:
        insights.append("Overall demo wellness score is low. Review sleep, activity, stress, and hydration trends.")

    return insights
