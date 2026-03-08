import joblib
import pandas as pd

# load trained model
model = joblib.load("artifacts/churn_model.pkl")

# sample customer data
sample = {
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 5,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 70,
    "TotalCharges": 350
}

df = pd.DataFrame([sample])

prediction = model.predict(df)

if prediction[0] == 1:
    print("Customer will churn")
else:
    print("Customer will stay")