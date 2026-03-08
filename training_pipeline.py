from src.data_loader import DataLoader
from src.preprocessing import Preprocessing
from src.model_training import ModelTraining
from src.model_evaluation import ModelEvaluation

def run_pipeline():

    df = DataLoader().load_data("data/churn.csv")

    df = Preprocessing().transform(df)

    model, X_test, y_test = ModelTraining().train(df)

    accuracy = ModelEvaluation().evaluate(model, X_test, y_test)

    print("Model Accuracy:", accuracy)
