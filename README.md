# 🏥 Insurance Cost Prediction App

A sleek and interactive **Streamlit web app** that predicts medical insurance costs based on user inputs like age, gender, BMI, children, smoking status, and region.

> 📊 Explore the data, build machine learning models, compare performance, and make live predictions — all in one place.

---

## 🚀 Live Demo

👉 [Check out the live app here](https://insurance-prediction-ga3aaamehue9pekqbmhc6a.streamlit.app/)

---

## 🧠 Features

- 📌 **EDA (Exploratory Data Analysis)**  
  Visualize trends, distributions, and correlations using Plotly and Seaborn.

- 🤖 **Model Building**  
  Train multiple ML models including Linear Regression, Random Forest, and XGBoost.

- ⚔️ **Model Comparison**  
  Compare model performance metrics like RMSE, R², MAE to pick the best one.

- 🔮 **Prediction Page**  
  Input custom data and get real-time insurance cost predictions.

---

## 🗃️ Dataset

The dataset used is `insurance.csv`, which includes:

- `age`
- `sex`
- `bmi`
- `children`
- `smoker`
- `region`
- `charges` *(target)*

---

## 🛠️ Tech Stack

- 🐍 Python 3.x  
- 📊 Pandas, NumPy, Seaborn, Plotly, Scikit-learn  
- 🚀 Streamlit  
- ☁️ Deployed on Streamlit Cloud

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/insurance-cost-prediction.git
cd insurance-cost-prediction
pip install -r requirements.txt
streamlit run app.py
