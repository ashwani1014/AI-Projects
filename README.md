# 🤖 AI Learning Journey

Welcome to my **AI Learning Journey** 🚀

This repository contains my learning progress, practical projects, experiments, and implementations as I learn **Artificial Intelligence from scratch**.

I am focusing on learning concepts practically by building projects instead of only studying theory.

---

## 📚 Learning Roadmap

### ✅ Week 1 — Python, Data Analysis & EDA

**Concepts Learned:**
- AI vs ML vs DL vs GenAI
- NumPy & Pandas for Data Manipulation
- Probability & Statistics Fundamentals (Mean, Median, Variance, Standard Deviation, Percentiles)
- Data Cleaning (Handling Missing Values, Removing Duplicates)
- Outlier Detection (IQR Method)
- Data Visualization with Matplotlib & Seaborn
- Exploratory Data Analysis (EDA) Best Practices

#### 🏠 Project — Ames Housing EDA
Applied the concepts learned during Week 1 to analyze and clean the Ames Housing dataset to uncover housing price trends.

- **Main Question:** *What factors influence house sale prices?*
- **Tasks Performed:** Dataset exploration, missing value imputation, outlier detection, correlation analysis, and visualization.
- **Tools Used:** Python, NumPy, Pandas, Matplotlib, Seaborn, Google Colab.

---

### ✅ Week 2 — Machine Learning & Classification Pipelines

**Concepts Learned:**
- Supervised Machine Learning Fundamentals
- Regression vs. Classification
- Evaluation Metrics (Accuracy, Precision, Recall, F1-Score)
- Feature Scaling (`StandardScaler`) & Scikit-Learn `Pipeline`
- Classification Algorithms:
  - Logistic Regression
  - K-Nearest Neighbors (KNN)
  - Support Vector Machines (SVM)
- Model Validation & Cross-Validation (`cross_val_score`, Stratified Splits)
- Hyperparameter Optimization (`GridSearchCV`)

#### 📈 Project 1 — House Price Prediction
Implemented regression models to predict housing prices using key real-estate indicators and regression evaluation techniques.

#### 🎓 Project 2 — Student Performance & Attendance Predictor
Built a complete end-to-end classification system to predict student outcomes based on study hours, attendance, prior scores, and sleep schedule.
- **Workflow:** Data Preprocessing ➔ ML Pipelines ➔ Cross Validation ➔ KNN Hyperparameter Tuning ➔ Model Serialization ➔ Streamlit Web App.
- **Tools Used:** Python, Scikit-Learn, Pandas, NumPy, Joblib, Streamlit.

---

## 📂 Repository Structure

```text
AI-Projects/
├── Week1/
│   ├── Ames_Housing_EDA.csv
│   └── EDA_Project.ipynb
├── Week2/
│   ├── Attendance_Project/
│   │   ├── data/
│   │   │   └── students.csv
│   │   ├── models/
│   │   │   └── student_models.pkl
│   │   ├── app.py
│   │   ├── train.py
│   │   ├── requirement.txt
│   │   └── README.MD
│   ├── Machine_Learning_House_Price_Prediction.ipynb
│   └── Tune_with_CV.ipynb
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack & Libraries
- **Language:** Python 3.x
- **Data Science:** NumPy, Pandas, Scipy
- **Machine Learning:** Scikit-Learn
- **Visualization:** Matplotlib, Seaborn
- **Deployment & UI:** Streamlit
