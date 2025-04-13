import pandas as pd
from sklearn.cluster import KMeans
import joblib
import logging
import os

logger = logging.getLogger(__name__)

def train_and_save_model(data, n_clusters=5):
    try:
        # Drop Customer_ID and encode Gender
        df = data.copy()
        df = df.drop(columns=["Customer_ID"])
        df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})

        model = KMeans(n_clusters=n_clusters, random_state=42)
        model.fit(df)

        os.makedirs("models", exist_ok=True)
        joblib.dump(model, "models/kmeans_model.pkl")
        logger.info("KMeans model trained and saved.")
        return model
    except Exception as e:
        logger.error(f"Error training model: {e}")
        raise

