import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

st.title("🥊 Model Comparison")

df = pd.read_csv("insurance.csv")
le = LabelEncoder()
for col in ['sex', 'smoker', 'region']:
    df[col] = le.fit_transform(df[col])

X = df.drop("charges", axis=1)
y = df["charges"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(),
    "Random Forest": RandomForestRegressor()
}

scores = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    score = r2_score(y_test, preds)
    scores[name] = score

# Plot
st.subheader("📈 R² Score Comparison")
fig, ax = plt.subplots()
ax.bar(scores.keys(), scores.values(), color=["#36a2eb", "#ff6384", "#4bc0c0"])
ax.set_ylabel("R² Score")
st.pyplot(fig)

best_model = max(scores, key=scores.get)
st.success(f"🏆 Best Performing Model: **{best_model}**")
