import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

st.title("🔮 Predict Insurance Charges")

df = pd.read_csv("insurance.csv")
le_sex = LabelEncoder().fit(df["sex"])
le_smoker = LabelEncoder().fit(df["smoker"])
le_region = LabelEncoder().fit(df["region"])

df["sex"] = le_sex.transform(df["sex"])
df["smoker"] = le_smoker.transform(df["smoker"])
df["region"] = le_region.transform(df["region"])

X = df.drop("charges", axis=1)
y = df["charges"]

model = LinearRegression()
model.fit(X, y)

# Input form
st.subheader("🧾 Enter Customer Info")
age = st.slider("Age", 18, 64, 30)
sex = st.selectbox("Sex", le_sex.classes_)
bmi = st.slider("BMI", 15.0, 45.0, 22.0)
children = st.slider("Children", 0, 5, 1)
smoker = st.selectbox("Smoker", le_smoker.classes_)
region = st.selectbox("Region", le_region.classes_)

input_df = pd.DataFrame([{
    "age": age,
    "sex": le_sex.transform([sex])[0],
    "bmi": bmi,
    "children": children,
    "smoker": le_smoker.transform([smoker])[0],
    "region": le_region.transform([region])[0]
}])

if st.button("🚀 Predict"):
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Predicted Charges: **${prediction:,.2f}**")
    st.balloons()

