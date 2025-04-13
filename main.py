from utils.logger import setup_logger
from utils.data_loader import load_data
from utils.model_trainer import train_and_save_model

def main():
    setup_logger()
    print("Starting clustering pipeline...")

    # Load the dataset
    df = load_data()

    # Train and save the model
    model = train_and_save_model(df, n_clusters=5)

    print("Model trained and saved to models/kmeans_model.pkl")

if __name__ == "__main__":
    main()
