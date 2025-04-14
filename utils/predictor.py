import pandas as pd
import joblib
from utils.logger import setup_logger

logger = setup_logger()

def load_model(model_path="models/kmeans_model.pkl"):
    try:
        model = joblib.load(model_path)
        logger.info("Model loaded successfully.")
        return model
    except Exception as e:
        logger.error(f"Failed to load model: {e}")
        raise

def prepare_input(gender, age, income, score):
    try:
        gender_encoded = 0 if gender == "Male" else 1
        input_data = pd.DataFrame([{
            "Gender": gender_encoded,
            "Age": age,
            "Annual_Income": income,
            "Spending_Score": score
        }])
        logger.info(f"Input prepared: {input_data.to_dict(orient='records')}")
        return input_data
    except Exception as e:
        logger.error(f"Failed to prepare input: {e}")
        raise

def predict_cluster(model, input_data):
    try:
        cluster = model.predict(input_data)[0]
        logger.info(f"Prediction made. Cluster: {cluster}")
        return cluster
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise
