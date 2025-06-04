import streamlit as st

st.set_page_config(page_title="Insurance ML Dashboard", page_icon="📊", layout="centered")

st.title("📊 Insurance Charges ML Dashboard")
st.markdown("Welcome to the complete ML app for predicting insurance charges.")
st.markdown("""
Use the sidebar to navigate through:
- EDA (Explore the dataset)
- Model Building (Train different models)
- Model Comparison (See who wins)
- Prediction (Try it out with custom inputs)
""")
st.success("Start by clicking one of the pages on the left! 🧭")


