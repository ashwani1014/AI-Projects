import streamlit as st
import torch
from PIL import Image
from torchvision import transforms
from pathlib import Path

from model import CatDogCNN


# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Cat vs Dog AI",
    page_icon="🐱",
    layout="centered"
)


# =========================================================
# 2. CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #64748b;
    margin-bottom: 30px;
}

.result-card {
    padding: 25px;
    border-radius: 20px;
    background: #ffffff;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    text-align: center;
    margin-top: 25px;
}

.prediction {
    font-size: 36px;
    font-weight: 800;
    margin: 10px;
}

.confidence {
    font-size: 20px;
    color: #475569;
}

.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 40px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. HEADER
# =========================================================

st.markdown(
    '<div class="title">🐱 Cat vs Dog AI 🐶</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Upload an image and let the CNN model identify it'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# 4. DEVICE
# =========================================================

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)


# =========================================================
# 5. MODEL PATH
# =========================================================

MODEL_PATH = Path("models/cat_dog_cnn.pth")


# =========================================================
# 6. LOAD TRAINED MODEL
# =========================================================

@st.cache_resource
def load_model():

    path_to_load = None

    # If app is run from project root
    if MODEL_PATH.exists():
        path_to_load = MODEL_PATH

    # Backup path if app is run from src folder
    elif Path("../models/cat_dog_cnn.pth").exists():
        path_to_load = Path("../models/cat_dog_cnn.pth")

    if path_to_load is None:
        return None

    model = CatDogCNN()

    model.load_state_dict(
        torch.load(
            path_to_load,
            map_location=device
        )
    )

    model.to(device)

    model.eval()

    return model


model = load_model()


# =========================================================
# 7. CHECK MODEL
# =========================================================

if model is None:

    st.error(
        "⚠️ Model weights not found: "
        "models/cat_dog_cnn.pth"
    )

    st.info(
        "Please train the model first using: "
        "python src/train.py"
    )

    st.stop()


# =========================================================
# 8. IMAGE PREPROCESSING
# =========================================================

transform = transforms.Compose([

    transforms.Resize((224, 224)),

    transforms.ToTensor(),

    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


# =========================================================
# 9. IMAGE UPLOADER
# =========================================================

uploaded_file = st.file_uploader(
    "📤 Upload a Cat or Dog image",
    type=["jpg", "jpeg", "png"]
)


# =========================================================
# 10. PREDICTION
# =========================================================

if uploaded_file is not None:

    # Open uploaded image
    image = Image.open(uploaded_file).convert("RGB")

    # Display image
    st.image(
        image,
        caption="Uploaded Image",
        width="stretch"
    )

    st.markdown("---")

    # Predict button
    if st.button(
        "🔍 Predict Image",
        width="stretch"
    ):

        with st.spinner(
            "🤖 AI is analyzing the image..."
        ):

            # ---------------------------------------------
            # Preprocess image
            # ---------------------------------------------

            image_tensor = transform(image)

            # Add batch dimension
            image_tensor = image_tensor.unsqueeze(0)

            # Move image to CPU/GPU
            image_tensor = image_tensor.to(device)


            # ---------------------------------------------
            # Model Prediction
            # ---------------------------------------------

            with torch.no_grad():

                outputs = model(image_tensor)

                # Convert model scores into probabilities
                probabilities = torch.softmax(
                    outputs,
                    dim=1
                )

                # Get highest probability
                confidence, predicted = torch.max(
                    probabilities,
                    1
                )


            # ---------------------------------------------
            # Get Class
            # ---------------------------------------------

            classes = ["Cat", "Dog"]

            prediction = classes[
                predicted.item()
            ]

            confidence_percentage = (
                confidence.item() * 100
            )


        # =================================================
        # RESULT
        # =================================================

        if prediction == "Cat":

            emoji = "🐱"

        else:

            emoji = "🐶"


        st.markdown(
            f"""
            <div class="result-card">

                <div class="prediction">
                    {emoji} {prediction}
                </div>

                <div class="confidence">
                    Confidence:
                    <strong>
                        {confidence_percentage:.2f}%
                    </strong>
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# 11. FOOTER
# =========================================================

st.markdown(
    '<div class="footer">'
    'Built with PyTorch + CNN + Streamlit'
    '</div>',
    unsafe_allow_html=True
)