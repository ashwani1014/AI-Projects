import time
import textwrap
from pathlib import Path
from PIL import Image
import streamlit as st
import torch
import torch.nn.functional as F
from torchvision import transforms

from model import CatDogCNN


# =========================================================
# 1. PAGE SETUP
# =========================================================

st.set_page_config(
    page_title="VisionAI · Cat vs Dog Neural Classifier",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="expanded"
)


def render_html(html_content: str):
    """Safely renders HTML without markdown converting leading whitespace to code blocks."""
    st.markdown(textwrap.dedent(html_content).strip(), unsafe_allow_html=True)


# =========================================================
# 2. ULTRA-SLICK MODERN OBSIDIAN THEME
# =========================================================

render_html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap');

/* Preserve Streamlit Material Icons */
[data-testid="stIconMaterial"],
[class*="material-symbols"],
[class*="material-icons"],
button span[class*="material"] {
    font-family: 'Material Symbols Rounded', 'Material Icons' !important;
}

/* Background Atmosphere - Slick Obsidian Canvas */
[data-testid="stAppViewContainer"] {
    background: 
        radial-gradient(circle at 12% 15%, rgba(99, 102, 241, 0.15) 0%, transparent 40%),
        radial-gradient(circle at 88% 85%, rgba(168, 85, 247, 0.12) 0%, transparent 40%),
        radial-gradient(circle at 50% 50%, rgba(14, 165, 233, 0.08) 0%, transparent 50%),
        #080a10 !important;
    color: #f1f5f9 !important;
}

[data-testid="stSidebar"] {
    background: rgba(12, 16, 26, 0.95) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.07) !important;
    backdrop-filter: blur(20px);
}

.block-container {
    max-width: 1140px !important;
    padding-top: 1.8rem !important;
    padding-bottom: 3rem !important;
}

header[data-testid="stHeader"] {
    background: transparent !important;
}

/* Typography Overrides */
[data-testid="stMetricValue"] {
    color: #f8fafc !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 700 !important;
}

[data-testid="stMetricLabel"] {
    color: #94a3b8 !important;
    font-weight: 600 !important;
    font-size: 13px !important;
}

[data-testid="stMarkdownContainer"] h4,
[data-testid="stMarkdownContainer"] h3 {
    color: #f8fafc !important;
    font-family: 'Outfit', sans-serif !important;
}

[data-testid="stWidgetLabel"] label,
[data-testid="stWidgetLabel"] p {
    color: #cbd5e1 !important;
}

/* Sidebar Brand Header */
.sidebar-brand {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 6px 0 16px 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    margin-bottom: 20px;
}

.brand-icon {
    font-size: 26px;
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.25), rgba(168, 85, 247, 0.25));
    border: 1px solid rgba(99, 102, 241, 0.4);
    border-radius: 14px;
    box-shadow: 0 4px 20px rgba(99, 102, 241, 0.25);
}

.brand-title {
    font-family: 'Outfit', sans-serif;
    font-size: 20px;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.2;
}

.brand-badge {
    font-size: 11px;
    font-weight: 700;
    color: #818cf8;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}

/* Sidebar Info Cards */
.side-card {
    background: rgba(18, 24, 38, 0.65);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 14px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

.side-label {
    font-size: 11px;
    font-weight: 700;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    margin-bottom: 4px;
}

.side-val {
    font-size: 14px;
    font-weight: 700;
    color: #f8fafc;
    display: flex;
    align-items: center;
    gap: 8px;
}

.live-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #10b981;
    box-shadow: 0 0 10px #10b981;
    display: inline-block;
}

.arch-tag {
    display: inline-block;
    background: rgba(99, 102, 241, 0.15);
    border: 1px solid rgba(99, 102, 241, 0.35);
    color: #c7d2fe;
    font-size: 11px;
    font-weight: 600;
    padding: 3px 8px;
    border-radius: 6px;
    margin: 2px 2px;
    font-family: 'JetBrains Mono', monospace;
}

/* Hero Section */
.hero-box {
    text-align: center;
    padding: 15px 10px 25px 10px;
}

.badge-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(99, 102, 241, 0.14);
    border: 1px solid rgba(99, 102, 241, 0.35);
    color: #c7d2fe;
    font-size: 12px;
    font-weight: 700;
    padding: 6px 18px;
    border-radius: 9999px;
    margin-bottom: 14px;
    letter-spacing: 0.6px;
    text-transform: uppercase;
    box-shadow: 0 0 25px rgba(99, 102, 241, 0.15);
}

.hero-h1 {
    font-family: 'Outfit', sans-serif;
    font-size: 50px;
    font-weight: 900;
    letter-spacing: -1.2px;
    background: linear-gradient(135deg, #ffffff 15%, #cbd5e1 45%, #818cf8 75%, #c084fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    line-height: 1.15;
    filter: drop-shadow(0 4px 20px rgba(99, 102, 241, 0.25));
}

.hero-p {
    font-size: 16px;
    color: #94a3b8;
    max-width: 620px;
    margin: 12px auto 0 auto;
    line-height: 1.6;
}

/* Image preview styling */
[data-testid="stImage"] img {
    border-radius: 18px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.6) !important;
}

/* File Uploader override */
[data-testid="stFileUploaderDropzone"] {
    background: rgba(18, 24, 38, 0.5) !important;
    border: 2px dashed rgba(99, 102, 241, 0.35) !important;
    border-radius: 18px !important;
    padding: 24px 20px !important;
    transition: all 0.2s ease !important;
}

[data-testid="stFileUploaderDropzone"]:hover {
    border-color: rgba(168, 85, 247, 0.6) !important;
    background: rgba(18, 24, 38, 0.75) !important;
}

/* Glass Card */
.glass-box {
    background: rgba(18, 24, 38, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(16px);
    border-radius: 20px;
    padding: 24px;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
}

/* Result Banners */
.result-banner-cat {
    background: linear-gradient(135deg, rgba(244, 63, 94, 0.18) 0%, rgba(217, 70, 239, 0.1) 100%);
    border: 2px solid rgba(244, 63, 94, 0.55);
    border-radius: 20px;
    padding: 24px;
    text-align: center;
    box-shadow: 0 15px 40px -5px rgba(244, 63, 94, 0.35);
    margin-bottom: 18px;
}

.result-banner-dog {
    background: linear-gradient(135deg, rgba(14, 165, 233, 0.18) 0%, rgba(99, 102, 241, 0.1) 100%);
    border: 2px solid rgba(56, 189, 248, 0.55);
    border-radius: 20px;
    padding: 24px;
    text-align: center;
    box-shadow: 0 15px 40px -5px rgba(56, 189, 248, 0.35);
    margin-bottom: 18px;
}

.result-avatar {
    font-size: 64px;
    margin-bottom: 4px;
    filter: drop-shadow(0 6px 15px rgba(0, 0, 0, 0.4));
}

.result-name {
    font-family: 'Outfit', sans-serif;
    font-size: 34px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 6px;
}

.conf-badge {
    display: inline-block;
    padding: 6px 20px;
    border-radius: 9999px;
    background: rgba(0, 0, 0, 0.45);
    border: 1px solid rgba(255, 255, 255, 0.15);
    font-size: 15px;
    font-weight: 700;
    color: #ffffff;
    font-family: 'JetBrains Mono', monospace;
}

/* Predict Button */
.stButton > button {
    width: 100% !important;
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #d946ef 100%) !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    padding: 13px 24px !important;
    border-radius: 14px !important;
    border: none !important;
    box-shadow: 0 6px 20px rgba(99, 102, 241, 0.35) !important;
    transition: all 0.2s ease !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 28px rgba(168, 85, 247, 0.5) !important;
}

/* Footer */
.footer-text {
    text-align: center;
    color: #64748b;
    font-size: 13px;
    padding: 35px 0 10px 0;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
    margin-top: 40px;
}
</style>
""")


# =========================================================
# 3. DEVICE & MODEL SETUP
# =========================================================

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
device_name = "NVIDIA CUDA GPU ⚡" if torch.cuda.is_available() else "CPU 💻"

MODEL_PATH = Path("models/cat_dog_cnn.pth")


@st.cache_resource
def load_model():
    path_to_load = None
    if MODEL_PATH.exists():
        path_to_load = MODEL_PATH
    elif Path("../models/cat_dog_cnn.pth").exists():
        path_to_load = Path("../models/cat_dog_cnn.pth")

    if path_to_load is None:
        return None

    model = CatDogCNN()
    model.load_state_dict(
        torch.load(path_to_load, map_location=device)
    )
    model.to(device)
    model.eval()
    return model


model = load_model()


# =========================================================
# 4. ENHANCED SLICK SIDEBAR
# =========================================================

with st.sidebar:
    render_html("""
    <div class="sidebar-brand">
        <div class="brand-icon">🐾</div>
        <div>
            <div class="brand-title">Cat vs Dog AI</div>
            <div class="brand-badge">Vision Studio</div>
        </div>
    </div>
    """)

    render_html(f"""
    <div class="side-card">
        <div class="side-label">Inference Engine</div>
        <div class="side-val">
            <span class="live-dot"></span>
            <span>{device_name}</span>
        </div>
    </div>
    """)

    render_html("""
    <div class="side-card">
        <div class="side-label">Model Architecture</div>
        <div style="font-weight: 700; font-size: 14px; margin-bottom: 8px; color: #f8fafc;">
            Custom 2-Block CNN
        </div>
        <div style="line-height: 1.8;">
            <span class="arch-tag">Conv2D(32)</span>
            <span class="arch-tag">ReLU</span>
            <span class="arch-tag">MaxPool</span><br>
            <span class="arch-tag">Conv2D(64)</span>
            <span class="arch-tag">ReLU</span>
            <span class="arch-tag">MaxPool</span><br>
            <span class="arch-tag">Linear(128)</span>
            <span class="arch-tag">Softmax(2)</span>
        </div>
    </div>
    """)

    st.markdown("#### 🎛️ Settings")
    auto_predict = st.toggle("⚡ Auto-Predict on Upload", value=True)
    show_distribution = st.toggle("📊 Probability Breakdown", value=True)
    celebrate_effect = st.toggle("🎉 Match Notification", value=True)

    st.markdown("---")

    render_html("""
    <div class="side-card" style="background: rgba(99, 102, 241, 0.08); border-color: rgba(99, 102, 241, 0.25);">
        <div class="side-label" style="color: #a5b4fc;">💡 Best Results Tip</div>
        <div style="font-size: 12px; color: #cbd5e1; line-height: 1.5; margin-top: 4px;">
            • Use clear, single-subject pet photos<br>
            • Optimal image resolution: 224×224 px<br>
            • Formats: JPG, PNG, WEBP
        </div>
    </div>
    """)


# =========================================================
# 5. HERO HEADER
# =========================================================

render_html("""
<div class="hero-box">
    <div class="badge-pill">
        <span>⚡ Deep Learning · PyTorch CNN</span>
    </div>
    <h1 class="hero-h1">Cat vs Dog AI Classifier</h1>
    <p class="hero-p">
        Upload a pet picture to classify whether it's a <strong>Cat</strong> or a <strong>Dog</strong>
        with instant neural feature extraction and confidence analysis.
    </p>
</div>
""")


# =========================================================
# 6. MODEL CHECK
# =========================================================

if model is None:
    st.error("⚠️ **Model Weights Missing!** Could not locate `models/cat_dog_cnn.pth`.")
    st.info("Please train the model first:\n```bash\npython src/train.py\n```")
    st.stop()


# =========================================================
# 7. IMAGE PREPROCESSING
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
# 8. UPLOAD INTERFACE
# =========================================================

uploaded_file = st.file_uploader(
    "Upload a Cat or Dog Image (JPG, PNG, WEBP)",
    type=["jpg", "jpeg", "png", "webp"],
    help="Upload a clear pet photo to analyze."
)


# =========================================================
# 9. RESULTS & PREDICTION
# =========================================================

if uploaded_file is not None:
    raw_img = Image.open(uploaded_file)
    image = raw_img.convert("RGB") if raw_img.mode != "RGB" else raw_img

    render_html("<div style='margin-top: 25px;'></div>")
    col_img, col_result = st.columns([1, 1.15], gap="large")

    with col_img:
        st.markdown("#### 📷 Image Preview")
        st.image(image, use_container_width=True)

        col_res, col_chan = st.columns(2)
        with col_res:
            st.metric(label="📐 Resolution", value=f"{image.width} × {image.height}")
        with col_chan:
            st.metric(label="🎨 Channels", value="3 (RGB)")

    with col_result:
        st.markdown("#### 🤖 AI Classification")

        should_predict = True
        if not auto_predict:
            should_predict = st.button("🔍 Run Prediction", key="manual_btn")

        if should_predict:
            start_clock = time.perf_counter()
            with st.spinner("Analyzing image features with CNN..."):
                img_tensor = transform(image).unsqueeze(0).to(device)

                with torch.no_grad():
                    logits = model(img_tensor)
                    probabilities = F.softmax(logits, dim=1)[0]
                    confidence, predicted = torch.max(probabilities, dim=0)

                latency_ms = (time.perf_counter() - start_clock) * 1000

                classes = ["Cat", "Dog"]
                prediction = classes[predicted.item()]
                confidence_pct = confidence.item() * 100
                cat_prob_pct = probabilities[0].item() * 100
                dog_prob_pct = probabilities[1].item() * 100

                is_cat = prediction == "Cat"
                banner_cls = "result-banner-cat" if is_cat else "result-banner-dog"
                emoji_icon = "🐱" if is_cat else "🐶"
                color_accent = "#fb7185" if is_cat else "#38bdf8"

                if celebrate_effect and confidence_pct >= 90.0:
                    st.toast(f"🎯 Match Identified: {prediction} ({confidence_pct:.1f}%)", icon="✨")

                # Verdict Card
                render_html(f"""
                <div class="{banner_cls}">
                    <div class="result-avatar">{emoji_icon}</div>
                    <div class="result-name">{prediction} Detected</div>
                    <div class="conf-badge">
                        Confidence: <strong style="color: {color_accent};">{confidence_pct:.2f}%</strong>
                    </div>
                </div>
                """)

                # Probability Breakdown in Percentages
                if show_distribution:
                    st.markdown("#### 📊 Prediction Probabilities")
                    col_cat, col_dog = st.columns(2)
                    with col_cat:
                        st.metric(
                            label="🐱 Cat Probability",
                            value=f"{cat_prob_pct:.1f}%"
                        )
                        st.progress(float(min(max(cat_prob_pct / 100.0, 0.0), 1.0)))

                    with col_dog:
                        st.metric(
                            label="🐶 Dog Probability",
                            value=f"{dog_prob_pct:.1f}%"
                        )
                        st.progress(float(min(max(dog_prob_pct / 100.0, 0.0), 1.0)))

                # Telemetry
                col_lat, col_eng = st.columns(2)
                with col_lat:
                    st.metric(label="⏱️ Inference Latency", value=f"{latency_ms:.1f} ms")
                with col_eng:
                    st.metric(label="⚙️ Compute Target", value=device.type.upper())

else:
    # Empty Placeholder
    render_html("""
    <div class="glass-box" style="text-align: center; padding: 50px 20px; margin-top: 25px;">
        <div style="font-size: 50px; margin-bottom: 10px;">🐾</div>
        <div style="font-family: 'Outfit'; font-size: 22px; font-weight: 800; color: #ffffff;">No Image Selected</div>
        <div style="font-size: 14px; color: #94a3b8; margin-top: 6px; max-width: 420px; margin-left: auto; margin-right: auto; line-height: 1.6;">
            Upload any cat or dog photo using the uploader above to view instant predictions and probability distribution.
        </div>
    </div>
    """)


# =========================================================
# 10. FOOTER
# =========================================================

render_html("""
<div class="footer-text">
    Crafted with ❤️ using <strong>PyTorch</strong> & <strong>Streamlit</strong> · Cat vs Dog AI
</div>
""")