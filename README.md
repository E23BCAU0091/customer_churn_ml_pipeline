Customer Churn Prediction ML Pipeline

This project implements a machine learning pipeline to predict customer churn using the Telco Customer Churn dataset.

Customer churn prediction helps telecom companies identify customers likely to leave their services, allowing them to take proactive retention measures.

The project demonstrates a modular ML pipeline architecture including data preprocessing, model training, evaluation, and prediction.

#Problem Statement:

Customer churn is a major challenge for telecom companies because losing customers directly affects revenue.

Using machine learning, companies can:

Identify customers likely to churn

Understand key factors influencing churn

Improve customer retention strategies


#Dataset:

The dataset used is the Telco Customer Churn dataset, which contains customer information such as:

customer demographics

service subscriptions

contract type

billing details

churn status

#Exploratory Data Analysis:

Churn Distribution

The dataset shows a class imbalance, where most customers do not churn.

Machine Learning Pipeline Architecture

The project follows a modular machine learning pipeline design.

#Pipeline Steps:

Data Loading

Data Preprocessing

Train-Test Split

Model Training

Model Evaluation

Prediction

#Model Training:

The project uses Random Forest Classifier for churn prediction.

Reasons for choosing Random Forest:

Works well with tabular data

Handles nonlinear relationships

Provides feature importance

Robust against overfitting

#Model Evaluation:

Model performance is evaluated using a confusion matrix.

This helps understand:

True Positives

True Negatives

False Positives

False Negatives

#Feature Importance:

Feature importance helps identify which features influence churn prediction the most.

Key factors affecting churn include:

TotalCharges

MonthlyCharges

tenure

Contract type

Payment method

#Project Structure:

customer_churn_ml_pipeline
│
├── main.py
├── predict.py
├── data_loader.py
├── preprocessing.py
├── model_training.py
├── model_evaluation.py
│
├── churn.csv
├── churn_model.pkl
├── requirements.txt
│
└── images
    ├── dataset_preview.png
    ├── churn_distribution.png
    ├── confusion_matrix.png
    ├── feature_importance.png
    └── ml_pipeline_architecture.png

   #Installation
    git clone https://github.com/E23BCAU0091/customer_churn_ml_pipeline.git
    cd customer_churn_ml_pipeline
    #Install dependencies:
    pip install -r requirements.txt

   Run the pipeline:
    python main.py
    python predict.py

 #Technologies Used

    -Python

    -Pandas

    -NumPy

    -Scikit-learn

    -Matplotlib

 #Future Improvements

    Hyperparameter tuning

    Model deployment using Flask or FastAPI

    Real-time churn prediction API

    Dashboard visualization

    Author

Harshita Jain
Data Science Student
