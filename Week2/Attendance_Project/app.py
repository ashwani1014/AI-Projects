import os
import joblib
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Student Performance & Attendance Predictor",
    page_icon="🎓",
    layout="wide"
)

# Custom Styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #4B5563;
        text-align: center;
        margin-bottom: 2rem;
    }
    .result-card-pass {
        padding: 1.5rem;
        border-radius: 12px;
        background-color: #ECFDF5;
        border: 2px solid #10B981;
        color: #065F46;
        text-align: center;
    }
    .result-card-fail {
        padding: 1.5rem;
        border-radius: 12px;
        background-color: #FEF2F2;
        border: 2px solid #EF4444;
        color: #991B1B;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🎓 Student Performance & Attendance Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Machine Learning model predicting student Pass / Fail outcome based on academic habits and attendance.</div>', unsafe_allow_html=True)

# Load Model
model_path = os.path.join(os.path.dirname(__file__), "models", "student_models.pkl")

@st.cache_resource
def load_model():
    if os.path.exists(model_path):
        return joblib.load(model_path)
    return None

model = load_model()

col_form, col_pred = st.columns([1.2, 1], gap="large")

with col_form:
    st.subheader("📋 Enter Student Details")
    
    hours = st.slider("Daily Study Hours", min_value=0.0, max_value=16.0, value=5.0, step=0.5)
    attendance = st.slider("Attendance Percentage (%)", min_value=0, max_value=100, value=75, step=1)
    previous_marks = st.slider("Previous Exam Marks", min_value=0, max_value=100, value=65, step=1)
    assignments = st.slider("Assignments Completed", min_value=0, max_value=10, value=6, step=1)
    sleep = st.slider("Daily Sleep Duration (Hours)", min_value=2.0, max_value=12.0, value=7.0, step=0.5)
    
    predict_btn = st.button("🚀 Predict Outcome", type="primary", use_container_width=True)

with col_pred:
    st.subheader("📊 Prediction Results")
    
    if model is None:
        st.warning("⚠️ Model not found. Please train the model first by running `python train.py`.")
    else:
        # Prepare input dataframe matching feature names
        input_data = pd.DataFrame([{
            "hours": hours,
            "attendance": attendance,
            "previous_marks": previous_marks,
            "assignments": assignments,
            "sleep": sleep
        }])
        
        prediction = model.predict(input_data)[0]
        
        if predict_btn:
            if prediction == 1:
                st.markdown(
                    """
                    <div class="result-card-pass">
                        <h2>🎉 Prediction: PASS</h2>
                        <p>The student is on track to pass based on their current academic metrics and attendance habits.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    """
                    <div class="result-card-fail">
                        <h2>⚠️ Prediction: FAIL / AT RISK</h2>
                        <p>The student may need additional academic support, improved attendance, or structured study plans.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            # Show input summary
            st.write("---")
            st.markdown("#### Input Features Summary")
            st.dataframe(input_data, use_container_width=True)
        else:
            st.info("👈 Adjust the student parameters on the left and click **Predict Outcome**.")
