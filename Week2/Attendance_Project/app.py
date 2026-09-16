import streamlit as st
import joblib


# Load trained model
model = joblib.load("models/student_models.pkl")


# Page title
st.title("🎓 Student Performance Predictor")

st.write("Enter the student's details to predict the result.")


# User inputs
hours = st.number_input(
    "Study Hours per Day",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

previous_marks = st.number_input(
    "Previous Marks (%)",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

assignments = st.number_input(
    "Assignments Completed",
    min_value=0,
    max_value=20,
    value=5
)

sleep = st.number_input(
    "Sleep Hours per Day",
    min_value=0.0,
    max_value=24.0,
    value=7.0
)


# Prediction button
if st.button("Predict Result"):

    # Create user input
    user_input = [[
        hours,
        attendance,
        previous_marks,
        assignments,
        sleep
    ]]

    # Make prediction
    prediction = model.predict(user_input)

    # Display result
    if prediction[0] == 1:
        st.success("✅ Student is likely to PASS")
    else:
        st.error("❌ Student is likely to FAIL")