# Customer Churn Prediction ML Pipeline

 Overview

This project builds a machine learning pipeline to predict customer churn using the Telco Customer Churn dataset.

The pipeline performs:

- Data loading
- Data preprocessing
- Model training
- Model evaluation
- Churn prediction

The goal is to identify customers likely to leave the service so businesses can take preventive actions.

# Project Structure

customer_churn_project
│
├── artifacts/
│ └── churn_model.pkl

├── data/
│ └── churn.csv

├── pipeline/
│ └── training_pipeline.py

├── src/
│ ├── data_loader.py
│ ├── preprocessing.py
│ ├── model_training.py
│ └── model_evaluation.py

├── main.py
└── predict.py

#Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib

# How to Run the Project

Clone the repository:
git clone https://github.com/your-username/customer_churn_ml_pipeline.git
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the training pipeline:

```
python main.py
```

Run prediction:

```
python predict.py
```

# Model Used

Random Forest Classifier

## Author

Harshita Jain
