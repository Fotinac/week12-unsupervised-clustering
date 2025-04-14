# UCLA Neural Network Admission Predictor

This application uses a trained neural network to predict graduate admission chances based on a candidate’s profile. Built with **Streamlit** and deployed on the **Streamlit Community Cloud**, the app offers real-time predictions through a simple user interface.

[Visit the app here](https://week12-unsupervised-clustering-4e9days6tedeifzd8nw8w4.streamlit.app))  

---

## Purpose

This project aims to help students evaluate their chances of admission to graduate programs based on features like GRE, TOEFL, CGPA, and university rating using a machine learning model trained on the *Admission.csv* dataset.

---

## Features

- Intuitive web UI powered by **Streamlit**.
- Interactive form for user input (GRE, TOEFL, CGPA, etc.).
- Neural network–based model predicts admission probability.
- Visual output and feature importance graph.
- Logging and error-handling implemented for robustness.
- Ready for cloud deployment via Streamlit Community Cloud.

---

## Dataset

The dataset used is `Admission.csv`, containing historical student admission profiles and outcomes. Features include:

- GRE Score  
- TOEFL Score  
- University Rating  
- Statement of Purpose (SOP)  
- Letter of Recommendation (LOR)  
- CGPA  
- Research Experience  
- Chance of Admit

---

## Technologies Used

- **Python**
- **Streamlit** – UI and deployment  
- **TensorFlow/Keras** – Neural network modeling  
- **Pandas & NumPy** – Data preprocessing  
- **Matplotlib** – Visualizations  
- **Scikit-learn** – Data splitting and metrics  
- **Logging** – Centralized logs for debugging  
- **VS Code & GitHub** – Development and version control

---

## Model

A feedforward neural network is trained to predict the probability of admission. It uses scaled inputs and evaluates performance on a test set. The model is saved as `admission_model.h5`.

---

## Installation & Setup (Local Deployment)

Follow the steps below to run the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Fotinac/week12-unsupervised-clustering.git
   cd ucla-admission-predictor
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```

---

## Logging

Application logs are stored in `logs/app.log`. All modules use a centralized logger from `utils/logger.py` for debugging and tracking execution flow.

---

## Future Enhancements

- Add model explainability using SHAP or LIME.
- Compare multiple model types.
- Enable batch uploads for multiple predictions.
- Display more advanced visualizations.

---

## Author

- **Name**: Fotinacao  
- **Course**: CST2216 — Business Intelligence System Infrastructure  
- **Instructor**: Swapnil Kangralkar  
- **Institution**: Algonquin College

---

## License

This project is for educational and demonstration purposes only.
