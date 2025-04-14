
# Mall Customer Segmentation App

This Streamlit application performs customer segmentation using unsupervised clustering techniques on the **Mall Customers dataset**. It helps identify distinct groups of customers based on their demographic and spending behaviors.

[Visit the app here](https://week12-unsupervised-clustering-4e9days6tedeifzd8nw8w4.streamlit.app)  

---

## Purpose

The goal of this project is to apply clustering algorithms (like K-Means) to segment mall customers into groups that share similar characteristics. These insights can help marketing teams target different customer segments more effectively.

---

## Features

- User-friendly web interface using **Streamlit**
- Input sliders to adjust cluster parameters
- Real-time clustering and visualization updates
- Displays:
  - Cluster plots
  - Customer count by cluster
  - Average spending and income per cluster
- Robust backend with logging and error handling

---

## Dataset

The dataset `mall_customers.csv` includes the following features:

- CustomerID  
- Gender  
- Age  
- Annual Income (k$)  
- Spending Score (1–100)

---

## Technologies Used

- **Streamlit** – For building the user interface
- **Pandas & NumPy** – For data manipulation
- **Scikit-learn** – For KMeans clustering
- **Matplotlib & Seaborn** – For visualizations
- **Logging** – For tracking app behavior
- **VS Code & GitHub** – Development & version control

---

## Model

The application uses **KMeans clustering** to segment customers. The number of clusters can be selected by the user. The model visualizes clusters using Age, Income, and Spending Score axes.

---

## Installation & Setup (Local Deployment)

Follow these steps to run the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Fotinac/week12-unsupervised-clustering.git
   cd week12-unsupervised-clustering
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

## Future Enhancements

- Enable dynamic clustering metric selection (e.g., silhouette score)
- Integrate DBSCAN or hierarchical clustering
- Upload custom datasets for segmentation
- Export cluster results to CSV

---

## Author

- **Name**: Fotinacao  
- **Course**: CST2216 — Business Intelligence System Infrastructure  
- **Instructor**: Swapnil Kangralkar  
- **Institution**: Algonquin College

---

## License

This project is for educational and demonstration purposes only.