AI Personal Health Tracker ❤️

An end-to-end Machine Learning application that analyzes fitness, diet, sleep, and lifestyle data to predict a wellness score, identify historical trends, and generate personalized health insights through an interactive Streamlit dashboard.

> **Disclaimer:** This project is created for educational and demonstration purposes. It is not a medical diagnostic or treatment system. The included dataset is synthetic.

## 🚀 Features

- AI-based wellness score prediction
- Random Forest Regression model
- Health data preprocessing using Pandas
- Historical weekly and monthly trend analysis
- Interactive Plotly charts
- AI-generated health insights
- Streamlit web dashboard
- Model evaluation using MAE, RMSE, and R²
- Saved trained model using Joblib
- Modular Python project structure
- Extensible architecture for external health-data integration

## 🧠 Machine Learning Workflow


Health Data
     ↓
Data Cleaning & Preprocessing
     ↓
Feature Engineering
     ↓
Train/Test Split
     ↓
Random Forest Regression
     ↓
Model Evaluation
     ↓
Wellness Score Prediction
     ↓
AI Health Insights
     ↓
Streamlit Dashboard
📊 Features Used

The model uses the following health and lifestyle features:

Sleep Hours
Daily Steps
Exercise Minutes
Water Intake
Calories
Protein Intake
Stress Level
Resting Heart Rate
BMI
Target Variable

wellness_score

The wellness score is a synthetic demonstration target calculated from multiple lifestyle indicators.

🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Random Forest Regression
Plotly
Streamlit
Joblib
Git
GitHub
📁 Project Structure
AI-Personal-Health-Tracker/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── health_data.csv
│
├── models/
│   ├── wellness_regression.joblib
│   └── metrics.json
│
└── src/
    ├── __init__.py
    ├── generate_data.py
    ├── train_model.py
    ├── predictor.py
    ├── trend_analysis.py
    ├── health_agent.py
    └── api_adapters.py
⚙️ Installation

Clone the repository:

git clone https://github.com/Shashwat-76/AI-Personal-Health-Tracker.git

Navigate to the project:

cd AI-Personal-Health-Tracker

Install the required dependencies:

pip install -r requirements.txt
▶️ Running the Project
1. Generate the health dataset
python src/generate_data.py

This creates the synthetic health dataset:

data/health_data.csv
2. Train the Machine Learning model
python src/train_model.py

The trained regression model is saved as:

models/wellness_regression.joblib

Model evaluation metrics are saved as:

models/metrics.json
3. Run the Streamlit application
python -m streamlit run app.py

The application will open in your browser.

📈 Model Evaluation

The regression model is evaluated using:

MAE

Mean Absolute Error measures the average absolute difference between actual and predicted wellness scores.

RMSE

Root Mean Squared Error measures prediction error while giving greater weight to larger errors.

R² Score

R² measures how much variation in the target variable is explained by the model.

Current Model Results
MAE  : 3.193
RMSE : 3.952
R²   : 0.657
🤖 AI Health Insight Agent

The project includes an AI-style insight layer that interprets user inputs and the predicted wellness score.

It can identify factors such as:

Low sleep duration
Low activity levels
Elevated stress
Low hydration
Higher resting heart rate
Overall wellness score category

The system generates easy-to-understand wellness observations based on the available data.

📊 Historical Trend Analysis

The application analyzes historical health data at weekly and monthly levels.

Weekly Analysis

The dashboard tracks:

Average wellness score
Average sleep
Average steps
Average exercise
Average stress
Monthly Analysis

Monthly aggregation helps identify longer-term changes in health and lifestyle patterns.

Interactive Plotly charts are used to visualize these trends.

🔌 External Health Data Integration

The project architecture includes an adapter layer that can be extended to support external health-data sources such as:

Fitbit
Apple Health
Google Fit
Health-data CSV exports

Actual production integrations would require the appropriate APIs, authentication, permissions, and provider-specific implementation.

💡 Key Learning Outcomes

This project demonstrates practical experience with:

Machine Learning
Regression
Data preprocessing
Feature engineering
Model evaluation
Model persistence
Historical data analysis
Data visualization
AI-based insight generation
Streamlit application development
Modular Python development
Git and GitHub
🔮 Future Improvements
Real Fitbit API integration
Apple Health integration
User authentication
Cloud database
Personalized model retraining
Advanced time-series forecasting
LLM-powered conversational health assistant
Docker deployment
Cloud deployment
Automated model monitoring
⚠️ Disclaimer

This application is intended for educational and demonstration purposes only.

It should not be used for medical diagnosis, treatment, or clinical decision-making.

The included health dataset is synthetic.

👨‍💻 Author

Shashwat Upadhyaya

B.Tech Computer Science Engineering
Specialization: Artificial Intelligence
Noida Institute of Engineering & Technology

GitHub: https://github.com/Shashwat-76
