# Live App  
[Click to open the app](https://week12unsupervisedclustering-3v8dmg9zmpl2bzxncwbpdi.streamlit.app) 

---

# Customer Segmentation App (Unsupervised Clustering)

This project is part of **CST2216 - Business Intelligence System Infrastructure** at Algonquin College (Week 12).

It demonstrates how to segment mall customers into behavioral clusters using **KMeans clustering** with a clean **Streamlit UI**, modular Python code, and deployment on **Streamlit Cloud**.

---

## Features

- Upload your own dataset or use the provided `mall_customers.csv`
- Interactive Streamlit interface with form-based input
- KMeans clustering with adjustable cluster number
- Predict cluster assignment for any new customer
- Visual feedback with bar chart
- Modular Python code with error handling and logging
- Beautiful color theme using Coolors palette
- Ready-to-deploy on Streamlit Cloud

---

## Project Structure

```
week12_unsupervised_clustering/
├── app_week12_cluster_ocean_v2.py  ← Streamlit UI app
├── main.py                         ← CLI script to train model
├── data/
│   └── mall_customers.csv          ← Dataset used for clustering
├── models/
│   └── kmeans_model.pkl            ← Trained model
├── logs/
│   └── app.log                     ← Runtime logging
├── utils/
│   ├── data_loader.py              ← Loads dataset
│   ├── model_trainer.py            ← Trains and saves KMeans model
│   ├── predictor.py                ← Makes predictions
│   ├── logger.py                   ← Logging setup
├── requirements.txt                ← All dependencies
├── README.md                       ← Project overview
```

---

## Requirements

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Run Locally

```bash
streamlit run app_week12_cluster_ocean_v2.py
```

---

## 👤 Author

- **Name**: Fotinacao  
- **Course**: CST2216 — Business Intelligence System Infrastructure  
- **Instructor**: Swapnil Kangralkar  
- **Institution**: Algonquin College

---

## License

This project is for educational and demonstration purposes only.
 
