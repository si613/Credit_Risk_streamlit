# 💳 Credit Risk Prediction & Customer Scoring App

This project is a **Streamlit web app** for predicting credit risk and estimating a customer's credit score using machine learning — specifically **XGBoost**, based on user-entered details.

---

## 🚀 Features

- Predicts the **probability of default** on a loan
- Estimates a **custom credit score** between 300–850
- Clean, responsive Streamlit UI with explanations and tooltips
- Uses a **pre-trained XGBoost model** (no retraining needed)
- Built with transparency: full dataset and notebooks included for review

---

## 📂 Repository Structure

| File / Folder              | Description |
|---------------------------|-------------|
| `streamlit_app.py`        | Final Streamlit app code for deployment |
| `train_model.ipynb`       | Notebook used to train and save the model + encoders |
| `credit_risk_dataset.csv` | Dataset used to train the model |
| `xgb_model.pkl`           | Trained XGBoost model (used in app) |
| `encoders.pkl`            | Label encoders for categorical features |
| `requirements.txt`        | List of dependencies for deployment |
| `README.md`               | You're reading it. |

---

## 🧠 Model Information

- Model used: `XGBClassifier`
- Dataset size: ~28,000 entries
- Features include:
  - Age, Income, Loan Amount, Interest Rate
  - Loan Purpose, Employment Length
  - Home Ownership, Credit History Length, etc.

---

## ⚙️ How to Run This App Locally

