import streamlit as st
import numpy as np
import joblib

# -----------------------------
# Load Trained Model
# -----------------------------
model = joblib.load("heart_disease_model.pkl")

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("❤️ Heart Disease Prediction")
st.write(
    "Enter the patient's medical information below to predict the likelihood of heart disease."
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("About Project")

st.sidebar.write("""
**Model:** Gaussian Naive Bayes

**Dataset:** UCI Heart Disease Dataset

**Features:** 13

**Target:**
- 0 = No Heart Disease
- 1 = Heart Disease
""")
st.sidebar.markdown("---")
st.sidebar.subheader("👨‍💻 Developer")
st.sidebar.success("Lohith")

# -----------------------------
# Two Columns
# -----------------------------
col1, col2 = st.columns(2)

# =============================
# LEFT COLUMN
# =============================
with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30
    )

    sex = st.radio(
        "Sex",
        ["Male", "Female"]
    )

    sex = 1 if sex == "Male" else 0

    cp = st.selectbox(
        "Chest Pain Type",
        [
            "Typical Angina",
            "Atypical Angina",
            "Non-anginal Pain",
            "Asymptomatic"
        ]
    )

    cp_mapping = {
        "Typical Angina": 0,
        "Atypical Angina": 1,
        "Non-anginal Pain": 2,
        "Asymptomatic": 3
    }

    cp = cp_mapping[cp]

    restecg = st.selectbox(
        "Resting ECG",
        [
            "Normal",
            "ST-T Wave Abnormality",
            "Left Ventricular Hypertrophy"
        ]
    )

    restecg_mapping = {
        "Normal": 0,
        "ST-T Wave Abnormality": 1,
        "Left Ventricular Hypertrophy": 2
    }

    restecg = restecg_mapping[restecg]

    exang = st.radio(
        "Exercise Induced Angina",
        ["No", "Yes"]
    )

    exang = 1 if exang == "Yes" else 0

    slope = st.selectbox(
        "Slope of Peak Exercise ST Segment",
        [
            "Upsloping",
            "Flat",
            "Downsloping"
        ]
    )

    slope_mapping = {
        "Upsloping": 0,
        "Flat": 1,
        "Downsloping": 2
    }

    slope = slope_mapping[slope]

    thal = st.selectbox(
        "Thalassemia",
        [
            "Normal",
            "Fixed Defect",
            "Reversible Defect"
        ]
    )

    thal_mapping = {
        "Normal": 1,
        "Fixed Defect": 2,
        "Reversible Defect": 3
    }

    thal = thal_mapping[thal]

# =============================
# RIGHT COLUMN
# =============================
with col2:

    trestbps = st.number_input(
        "Resting Blood Pressure (mm Hg)",
        min_value=80,
        max_value=250,
        value=120
    )

    chol = st.number_input(
        "Serum Cholesterol (mg/dl)",
        min_value=100,
        max_value=600,
        value=200
    )

    fbs = st.radio(
        "Fasting Blood Sugar > 120 mg/dl",
        ["No", "Yes"]
    )

    fbs = 1 if fbs == "Yes" else 0

    thalach = st.slider(
        "Maximum Heart Rate",
        min_value=50,
        max_value=220,
        value=150
    )

    oldpeak = st.slider(
        "Oldpeak",
        min_value=0.0,
        max_value=6.5,
        value=1.0,
        step=0.1
    )

    ca = st.selectbox(
        "Number of Major Vessels",
        [0, 1, 2, 3, 4]
    )

# -----------------------------
# Predict Button
# -----------------------------
if st.button("🔍 Predict"):

    patient_data = np.array([[
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]])

    prediction = model.predict(patient_data)

    probability = model.predict_proba(patient_data)

    st.markdown("---")
    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.error("⚠️ Heart Disease Detected")
        st.write(
            f"**Confidence:** {probability[0][1] * 100:.2f}%"
        )
    else:
        st.success("✅ No Heart Disease Detected")
        st.write(
            f"**Confidence:** {probability[0][0] * 100:.2f}%"
        )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.caption(
    "⚠️ This application is developed for educational purposes only and should not be used as a substitute for professional medical advice."
)