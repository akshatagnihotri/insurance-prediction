import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

st.title("🏗️ Model Building")

df = pd.read_csv("insurance.csv")
st.subheader("📄 Dataset Preview")

# Encode categorical variables
le = LabelEncoder()
for col in ['sex', 'smoker', 'region']:
    df[col] = le.fit_transform(df[col])

X = df.drop("charges", axis=1)
y = df["charges"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model_choice = st.selectbox("Choose a model", ["Linear Regression", "Decision Tree", "Random Forest"])

if model_choice == "Linear Regression":
    model = LinearRegression()
elif model_choice == "Decision Tree":
    model = DecisionTreeRegressor()
else:
    model = RandomForestRegressor()

model.fit(X_train, y_train)
score = model.score(X_test, y_test)

st.success(f"✅ {model_choice} trained successfully!")
st.write(f"🧠 Test R² Score: **{score:.3f}**")
st.subheader("📊 Model Coefficients (if applicable)")