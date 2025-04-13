import streamlit as st
from utils.logger import setup_logger
from utils.data_loader import load_data
from utils.predictor import load_model, prepare_input, predict_cluster
from utils.model_trainer import train_and_save_model
import pandas as pd
import matplotlib.pyplot as plt
import os

# Setup
st.set_page_config(page_title="🌊 Customer Clustering App", layout="centered")
setup_logger()

# Custom CSS with updated slider color
custom_css = '''
    <style>
        body {
            background-color: #caf0f8;
        }
        .main {
            background-color: #caf0f8;
        }
        h1, h2, h3, h4 {
            color: #03045E;
        }
        .stButton>button {
            background-color: #00B4D8;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            margin-top: 10px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #0077B6;
            color: white;
        }
        .stTextInput>div>div>input,
        .stSelectbox>div>div>div>div,
        .stNumberInput>div>input {
            border-color: #48CAE4;
        }
        /* Customize slider thumb and track */
        .stSlider > div[data-baseweb="slider"] > div {
            color: #0077B6;
        }
        .stSlider > div[data-baseweb="slider"] .css-1c5rxz0 {
            background: #0077B6;
        }
        .stSlider > div[data-baseweb="slider"] .css-14xtw13 {
            background: #caf0f8;
        }
        .stSlider > div[data-baseweb="slider"] .css-1t2x7v1 {
            background-color: #0077B6 !important;
        }
    </style>
'''
st.markdown(custom_css, unsafe_allow_html=True)

st.title("🛍️ Customer Segmentation (Unsupervised Clustering)")
st.markdown("Upload your customer data or use the default dataset to predict customer clusters.")

# Load dataset
use_default = st.toggle("Use Default Dataset", value=True)
if use_default:
    df = load_data()
else:
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        st.warning("Upload a file or use the default dataset.")
        st.stop()

# Sidebar training
with st.sidebar:
    st.markdown("## 🔧 Model Setup")
    n_clusters = st.slider("Number of Clusters", 2, 10, value=5)
    if st.button("Train KMeans Model"):
        model = train_and_save_model(df, n_clusters=n_clusters)
        st.success("Model trained and saved successfully!")

# Load model
if os.path.exists("models/kmeans_model.pkl"):
    model = load_model()
else:
    st.error("Model file not found. Please train the model first.")
    st.stop()

st.divider()
st.subheader("👤 Customer Input")

# User inputs
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 15, 80, 30)
income = st.number_input("Annual Income", min_value=0, value=60)
score = st.slider("Spending Score (1-100)", 1, 100, 50)

# Predict
if st.button("🎯 Predict Cluster"):
    input_df = prepare_input(gender, age, income, score)
    cluster = predict_cluster(model, input_df)

    st.success(f"🧩 The customer belongs to Cluster: `{cluster}`")

    st.markdown("### 📊 Cluster Visualization")
    fig, ax = plt.subplots()
    ax.bar(["Predicted Cluster"], [cluster], color="#0077B6")
    ax.set_ylabel("Cluster Index")
    st.pyplot(fig)

