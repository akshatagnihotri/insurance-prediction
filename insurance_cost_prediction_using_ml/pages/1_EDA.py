import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🔍 Exploratory Data Analysis")

df = pd.read_csv("insurance.csv")
st.subheader("📄 Dataset Preview")
st.dataframe(df)

st.subheader("🧮 Summary Stats")
st.write(df.describe())

st.subheader("🎯 Age vs Charges")
fig = px.scatter(df, x="age", y="charges", color="smoker", size="bmi", hover_data=["sex"])
st.plotly_chart(fig)

st.subheader("📊 BMI Distribution")
fig2 = px.histogram(df, x="bmi", color="smoker", nbins=30)
st.plotly_chart(fig2)
