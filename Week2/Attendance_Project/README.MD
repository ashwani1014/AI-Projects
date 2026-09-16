# 🎓 Student Performance & Attendance Prediction Project

This project predicts whether a student will **Pass** or **Fail** based on key factors like daily study hours, attendance percentage, previous exam scores, completed assignments, and sleep duration.

---

## 📌 Project Overview

- **Problem Type:** Binary Classification (Pass / Fail)
- **Algorithms Compared:**
  - Logistic Regression
  - K-Nearest Neighbors (KNN)
  - Support Vector Machines (SVM)
- **Techniques Used:**
  - Feature Scaling (`StandardScaler`) in `Pipeline`
  - Stratified Train/Test Split
  - 5-Fold Cross Validation (`cross_val_score`)
  - Hyperparameter Tuning via `GridSearchCV`
  - Model Persistence with `joblib`
  - Interactive UI with **Streamlit**

---

## 📁 Project Structure

```text
Attendance_Project/
├── data/
│   └── students.csv              # Student academic & attendance records
├── models/
│   └── student_models.pkl        # Serialized trained model pipeline
├── app.py                        # Streamlit web application
├── train.py                      # Data preprocessing, model training & evaluation script
├── requirement.txt               # Required Python dependencies
└── README.MD                     # Project documentation
```

---

## 🚀 How to Run

### 1. Install Dependencies
```bash
pip install -r requirement.txt
```

### 2. Train the Models
```bash
python train.py
```

### 3. Run the Streamlit Application
```bash
streamlit run app.py
```
