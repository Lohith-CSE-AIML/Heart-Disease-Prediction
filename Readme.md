# ❤️ Heart Disease Prediction using Machine Learning

## 📌 Overview

This project predicts whether a patient is likely to have **heart disease** based on medical information using a **Gaussian Naive Bayes Classifier**. It includes an interactive **Streamlit web application** where users can enter patient details and receive an instant prediction along with the model's confidence score.

---

## 🚀 Live Demo

**Streamlit App:** *https://heart-price-prediction-zslsk4qxugjhhkyqqbq7yw.streamlit.app*

---

## 📂 GitHub Repository

**Repository:** *https://github.com/Lohith-CSE-AIML/Heart-Price-Prediction.git*

---

## 📊 Dataset

* **Dataset:** UCI Heart Disease Dataset
* **Records:** 1,025
* **Features:** 13
* **Target Variable:**

  * **0** → No Heart Disease
  * **1** → Heart Disease

---

## 🧠 Machine Learning Model

After comparing multiple machine learning algorithms, **Gaussian Naive Bayes** was selected because it provided the best balance of performance on this dataset.

### Models Compared

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Decision Tree
* Random Forest
* Support Vector Machine (SVM)
* Gaussian Naive Bayes ✅
* Gradient Boosting

---

## 📋 Input Features

The application uses the following patient information:

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Serum Cholesterol
* Fasting Blood Sugar
* Resting ECG Results
* Maximum Heart Rate Achieved
* Exercise-Induced Angina
* ST Depression (Oldpeak)
* Slope of Peak Exercise ST Segment
* Number of Major Vessels
* Thalassemia

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn
* Joblib
* Streamlit

---

## ✨ Features

* Interactive Streamlit web application
* User-friendly interface with dropdown menus and sliders
* Instant heart disease prediction
* Prediction confidence score
* Clean and responsive UI
* Easy to use and beginner-friendly

---

## 📁 Project Structure

```text
Heart_Disease_Prediction/
│
├── app.py                     # Streamlit application
├── Heart_disease_prediction.ipynb
├── heart_disease_model.pkl    # Trained Gaussian Naive Bayes model
├── requirements.txt
├── README.md
└── dataset.csv
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone <https://github.com/Lohith-CSE-AIML/Heart-Price-Prediction.git>
```

### Move into the project folder

```bash
cd Heart_Disease_Prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📈 Workflow

1. Load the Heart Disease dataset.
2. Perform data preprocessing and exploratory data analysis (EDA).
3. Split the dataset into training and testing sets.
4. Train multiple machine learning models.
5. Evaluate model performance using Accuracy, Precision, Recall, F1-Score, and ROC-AUC.
6. Select the Gaussian Naive Bayes model.
7. Save the trained model using Joblib.
8. Build an interactive Streamlit application.
9. Predict heart disease based on user inputs.

---

## 📊 Evaluation Metrics

The model was evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC

---
---

## 📸 Application Preview


---

## ⚠️ Disclaimer

This project is developed for **educational purposes only**. It is not intended to replace professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional for medical decisions.

---

## 👨‍💻 Author

**Lohith**

* GitHub: https://github.com/Lohith-CSE-AIML
* LinkedIn: *www.linkedin.com/in/thoti-lohith*

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub. It helps others discover the project and motivates further improvements.
