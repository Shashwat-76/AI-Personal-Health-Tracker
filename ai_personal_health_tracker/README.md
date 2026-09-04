# AI Personal Health Tracker

An interview-ready machine learning project that analyzes fitness, diet, sleep, and lifestyle data, predicts a wellness score using regression, performs historical trend analysis, and provides an AI-style health insight agent through a Streamlit dashboard.

> **Important:** This project is for educational/demo purposes and is not a medical diagnostic tool. The included dataset is synthetic. Fitbit/Apple Health integrations are represented as optional adapters/interfaces rather than real authenticated integrations.

## Features
- Synthetic health dataset for reproducible demos
- Pandas-based cleaning and preprocessing
- Regression model to predict a wellness score
- Historical weekly/monthly trend analysis
- Interactive Plotly charts
- AI insight agent that explains trends and suggests general wellness actions
- Streamlit interface
- Model persistence with Joblib
- Modular project structure

## Tech Stack
Python, Pandas, NumPy, Scikit-learn, Plotly, Streamlit, Joblib

## Run locally
```bash
pip install -r requirements.txt
python src/generate_data.py
python src/train_model.py
streamlit run app.py
```

## Project structure
```text
ai_personal_health_tracker/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── health_data.csv
├── models/
│   └── wellness_regression.joblib
└── src/
    ├── generate_data.py
    ├── train_model.py
    ├── predictor.py
    ├── trend_analysis.py
    └── health_agent.py
```

## ML approach
The target variable is a synthetic **wellness score (0-100)** derived from sleep, activity, hydration, nutrition, stress, resting heart rate, and BMI. A Random Forest regression model learns the relationship between these features and the score. The goal is to demonstrate an end-to-end ML application rather than provide clinical prediction.

## Interview talking points
1. Data is generated in a reproducible way and can be replaced with real exports.
2. The model is trained only on the training split and evaluated on unseen test data.
3. Historical trend analysis aggregates daily observations into weekly/monthly views.
4. The agent separates model output from explanatory recommendations.
5. The dashboard makes the ML output understandable to a non-technical user.
