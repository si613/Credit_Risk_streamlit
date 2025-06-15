# 💳 Credit Risk Prediction & Customer Scoring App

A one-stop **Streamlit web app** that lets lenders (or curious borrowers) estimate **default risk** and generate a **credit-score–style rating** in real time.  
Built using a pre-trained **XGBoost** model selected after benchmarking multiple machine learning algorithms.

---

## 🎯 Purpose

This project serves as a **credit risk and scoring calculator** that provides instant insights into:
- The **likelihood of a customer defaulting on a loan**
- A derived **credit score between 300–850**, based on their financial profile

It combines **machine learning** with a user-friendly **web interface** to make risk scoring interpretable and accessible — for both education and application purposes.

---

## ⚙️ Process Overview

| Stage | What we did | Key Files |
|-------|-------------|-----------|
| **1. Exploratory Modelling** | Explored the dataset, visualized distributions, and compared ML models (Logistic Regression, Decision Tree, SVM, etc.). | `Credit Risk Prediction and Customer Scoring.ipynb` |
| **2. Chose Best Model** | Selected **XGBoost** based on ROC-AUC and overall performance. | — |
| **3. Final Training + Saving** | Used XGBoost to train the final model on all data, encoded categoricals using `LabelEncoder`, and saved everything using `pickle`. | `XGBoost Model_CreditRisk.ipynb` |
| **4. Streamlit App** | Built `streamlit_app.py` for real-time prediction UI with traffic-light risk visualization and score estimation. | `streamlit_app.py` |
| **5. Deployment Prep** | Created `requirements.txt`, organized repo, deployed to Streamlit Cloud. | `requirements.txt`, `README.md` |

---

## 📂 Repository Contents

| File                          | Description |
|-------------------------------|-------------|
| `Credit Risk Prediction and Customer Scoring.ipynb` | Exploratory analysis + comparison of various ML models |
| `XGBoost Model_CreditRisk.ipynb` | Trained XGBoost model + saved `xgb_model.pkl` and `encoders.pkl` |
| `credit_risk_dataset.csv`     | Raw dataset used for training (28k rows) |
| `streamlit_app.py`            | Streamlit app that loads the model and predicts |
| `xgb_model.pkl`               | Final trained XGBoost classifier |
| `encoders.pkl`                | Pickled LabelEncoders used for transforming inputs |
| `requirements.txt`            | Dependencies for local/cloud deployment |
| `README.md`                   | Project overview, setup, and documentation |

---

## 🌐 Streamlit Cloud Deployment

1. Push the repository to GitHub (public or private).
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud).
3. Click **New App** and connect your GitHub repo.
4. Set **main file path** to `streamlit_app.py`.
5. Click **Deploy**.
6. Wait a few seconds for the app to launch!

> **Note**: Make sure your repo includes `xgb_model.pkl`, `encoders.pkl`, and `requirements.txt` so the app can run without retraining.

---

## 🧠 Model & Dataset Info

- **Model**: `XGBClassifier` from `xgboost`
- **Input Features**:  
  - `person_age`, `person_income`, `person_home_ownership`,  
    `person_emp_length`, `loan_intent`, `loan_grade`,  
    `loan_amnt`, `loan_int_rate`, `loan_percent_income`,  
    `cb_person_default_on_file`, `cb_person_cred_hist_length`
- **Target Variable**: `loan_status` (0 = Non-default, 1 = Default)
- **Dataset Size**: 28,638 rows

---

## 🏔️ Challenges Faced

| Challenge | Resolution |
|----------|------------|
| **Slow prediction from retraining** | Shifted to using `pickle` to save/load model + encoders, avoiding retraining on every run |
| **Encoding mismatch** | Stored original `LabelEncoder` objects as `encoders.pkl` for consistent label mapping |
| **Imbalanced data** | Addressed using `scale_pos_weight` in XGBoost |
| **Streamlit UI clarity** | Used traffic-light coloring and score ranges to explain predictions |
| **Deployment packaging** | Ensured all key artifacts fit Streamlit Cloud size limits and function on cold start |

---

## 📉 Limitations

- No dynamic retraining — the model is fixed once trained
- Dataset limited to 11 features and a single institution’s records
- Credit score is **custom** — not calibrated to FICO or bureau benchmarks
- Imbalance in default vs. non-default classes can affect precision/recall

---

## 💡 Use Cases

- **Fintech prototypes** for quick pre-approval screening  
- **Consumer-facing credit tools** for awareness and education  
- **Teaching/learning resource** to understand ML deployment  
- **Loan origination teams** looking to integrate ML insights quickly  

---

## 📜 License

This project is for educational and demonstrative purposes only.  
Please fork and cite appropriately.

---

## ✅ Next Steps

- Add screenshots of the Streamlit UI in the repo (optional)
- Replace `your-username` in clone URL with your actual GitHub handle
- Share the deployed app link publicly or with teammates
- Extend the model or UI with new features like income bands, charts, etc.

---
