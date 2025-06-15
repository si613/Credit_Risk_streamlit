# streamlit_app.py
import streamlit as st

st.set_page_config(page_title="Credit Risk & Scoring System", layout="centered")

import pandas as pd
import numpy as np
import pickle
import os

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import roc_auc_score


# Load and preprocess data

@st.cache_resource
def load_model_and_encoders():
    with open("xgb_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("encoders.pkl", "rb") as f:
        encoders = pickle.load(f)
    return model, encoders

model, encoders = load_model_and_encoders()


# UI Design
st.markdown("""
    <style>
    .stApp {
        background-color: #0f1033;
        color: white;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)


st.title("💳 Credit Risk Prediction & Customer Scoring")
st.markdown("Enter your details to calculate **credit default risk** and generate a **custom credit score**.")

st.header("📋 User Input")

# Input form
with st.form("input_form"):
    age = st.slider("Age", 18, 100, 30)
    income = st.number_input("Annual Income (USD)", 1000, 500000, 50000, step=500)
    home_ownership = st.selectbox("Home Ownership", ["OWN", "RENT", "MORTGAGE", "OTHER"])
    emp_length = st.slider("Years of Employment", 0, 40, 5)
    loan_intent = st.selectbox("Loan Purpose", ["DEBTCONSOLIDATION", "EDUCATION", "HOMEIMPROVEMENT", "MEDICAL", "PERSONAL", "VENTURE"])
    loan_grade = st.selectbox("Loan Grade", list("ABCDEFG"))
    loan_amnt = st.number_input("Loan Amount", min_value=500, value=10000, step=500)
    loan_int_rate = st.slider("Interest Rate (%)", 0.0, 40.0, 10.0)
    loan_percent_income = loan_amnt / income
    default_on_file = st.selectbox("Any Previous Default on File?", ["Y", "N"])
    cred_hist_length = st.slider("Credit History Length (years)", 1, 30, 5)
    
    submit = st.form_submit_button("Predict Credit Risk & Score")

if submit:
    # Encode categorical inputs
    input_dict = {
        'person_age': age,
        'person_income': income,
        'person_home_ownership': encoders['person_home_ownership'].transform([home_ownership])[0],
        'person_emp_length': emp_length,
        'loan_intent': encoders['loan_intent'].transform([loan_intent])[0],
        'loan_grade': encoders['loan_grade'].transform([loan_grade])[0],
        'loan_amnt': loan_amnt,
        'loan_int_rate': loan_int_rate,
        'loan_percent_income': loan_percent_income,
        'cb_person_default_on_file': encoders['cb_person_default_on_file'].transform([default_on_file])[0],
        'cb_person_cred_hist_length': cred_hist_length
    }

    input_df = pd.DataFrame([input_dict])
    prob = model.predict_proba(input_df)[0][1]
    pred = model.predict(input_df)[0]

    # Credit Score Logic (custom scale: higher prob of default → lower score)
    credit_score = int(850 - (prob * 550))  # Range: 300–850

    # Output
    st.header("📊 Prediction Result")

    if prob > 0.05:
        st.error(f"⚠️ High Risk of Default (Probability: {prob:.2f})")
    else:
        st.success(f"✅ Low Risk of Default (Probability: {prob:.2f})")

    st.markdown(f"**💡 Estimated Credit Score: `{credit_score}`**")

    st.markdown("---")
    st.subheader("ℹ️ What This Means")
    st.markdown("""
    - A **credit score above 700** is typically considered good.
    - If you're **below 600**, you may face higher interest rates or rejections.
    - The default probability is calculated using historical loan default patterns.
    """)

