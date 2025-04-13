import os
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def load_data():
    try:
        path = os.path.join("data", "mall_customers.csv")
        df = pd.read_csv(path)
        logger.info("Data loaded successfully.")
        return df
    except FileNotFoundError:
        logger.error("Data file not found at data/mall_customers.csv")
        raise
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise
