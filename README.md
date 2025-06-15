# 💳 Credit Risk Prediction & Customer Scoring App

A one-stop **Streamlit web app** that lets lenders (or curious borrowers) estimate **default risk** and generate a **credit-score–style rating** in real time.  
Built using a pre-trained **XGBoost** model selected after benchmarking multiple machine learning algorithms.

---

# 🚀 Try the Credit Risk Prediction App

👉 **[Click here to open the app](https://creditriskapp-t9vwc9f5tfdtrfsnivakwu.streamlit.app/#credit-risk-prediction-customer-scoring)**

This Streamlit-powered app allows you to:
- Predict the risk of credit default
- Generate a personalized credit score
- Explore the financial health of a hypothetical applicant

No installation needed — just open the link above and try it out!

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

## 🚧 Challenges & Resolutions

| **Category**            | **Challenge**                                                                 | **Resolution**                                                                 |
|------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| 🧠 Model Management     | Serialized model (`xgb_model.pkl`) and encoders (`encoders.pkl`) reuse       | Used `@st.cache_resource` to efficiently load and reuse them                  |
| 💻 Streamlit Config     | Multiple calls to `st.set_page_config()` caused runtime errors                | Removed duplicate call, retained one at the top of the script                 |
| ☁️ Streamlit Cloud      | Dependency build failures (e.g., `pillow`, `scikit-learn`) due to versioning | Adjusted `requirements.txt` to include stable, compatible versions            |
| 📦 Dependency Conflicts | `numpy==2.0.0rc1` not available, caused `scikit-learn` build to fail          | Reverted to `scikit-learn==1.3.2` and compatible `numpy` version              |
| 🧵 Error Obfuscation    | Streamlit Cloud redacted traceback errors (`StreamlitAPIException`)          | Relied on log tab in "Manage app" to trace actual issue                       |



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

