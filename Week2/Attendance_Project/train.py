import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from sklearn.metrics import accuracy_score


# ==========================================
# 1. LOAD DATASET
# ==========================================

data_path = os.path.join(os.path.dirname(__file__), "data", "students.csv")
df = pd.read_csv(data_path)

print("Dataset:")
print(df.head())


# ==========================================
# 2. FEATURES AND TARGET
# ==========================================

X = df.drop("result", axis=1)
y = df["result"]


# ==========================================
# 3. TRAIN / TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ==========================================
# 4. LOGISTIC REGRESSION
# ==========================================

lr_model = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

lr_model.fit(X_train, y_train)

lr_pred = lr_model.predict(X_test)

lr_accuracy = accuracy_score(y_test, lr_pred)



# ==========================================
# 5. KNN
# ==========================================

knn_model = Pipeline([
    ("scaler", StandardScaler()),
    ("model", KNeighborsClassifier(n_neighbors=5))
])

knn_model.fit(X_train, y_train)

knn_pred = knn_model.predict(X_test)

knn_accuracy = accuracy_score(y_test, knn_pred)




# ==========================================
# 6. SVM
# ==========================================

from sklearn.calibration import CalibratedClassifierCV

svm_model = Pipeline([
    ("scaler", StandardScaler()),
    ("model", CalibratedClassifierCV(SVC(), ensemble=False))
])

svm_model.fit(X_train, y_train)

svm_pred = svm_model.predict(X_test)

svm_accuracy = accuracy_score(y_test, svm_pred)



# ==========================================
# 7. MODEL COMPARISON
# ==========================================

print("\n============================")
print("MODEL COMPARISON")
print("============================")

print("Logistic Regression:", lr_accuracy)
print("KNN:", knn_accuracy)
print("SVM:", svm_accuracy)



# ==========================================
# 8. CROSS VALIDATION
# ==========================================

lr_cv = cross_val_score(
    lr_model,
    X_train,
    y_train,
    cv=5,
    scoring="accuracy"
)

knn_cv = cross_val_score(
    knn_model,
    X_train,
    y_train,
    cv=5,
    scoring="accuracy"
)

svm_cv = cross_val_score(
    svm_model,
    X_train,
    y_train,
    cv=5,
    scoring="accuracy"
)


print("\n============================")
print("CROSS VALIDATION")
print("============================")

print("LR CV:", lr_cv)
print("LR Mean:", lr_cv.mean())

print("KNN CV:", knn_cv)
print("KNN Mean:", knn_cv.mean())

print("SVM CV:", svm_cv)
print("SVM Mean:", svm_cv.mean())


# ==========================================
# 9. KNN HYPERPARAMETER TUNING
# ==========================================

param_grid = {
    "model__n_neighbors": [3, 5, 7, 9, 11]
}

grid = GridSearchCV(
    knn_model,
    param_grid,
    cv=5,
    scoring="accuracy"
)

grid.fit(X_train, y_train)

print("\n============================")
print("KNN TUNING")
print("============================")

print("Best Parameters:", grid.best_params_)
print("Best CV Score:", grid.best_score_)

# ==========================================
# 10. SAVE BEST MODEL
# ==========================================
joblib.dump(grid.best_estimator_, "models/student_model.pkl")

print("Model saved successfully!")



