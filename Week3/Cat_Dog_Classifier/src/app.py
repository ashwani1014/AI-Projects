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
# 1. PAGE SETUP & CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="VisionAI · Cat vs Dog Neural Classifier",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="expanded"
)


def render_html(html_content: str):
    """Safely renders HTML without markdown treating leading whitespace as code blocks."""
    st.markdown(textwrap.dedent(html_content).strip(), unsafe_allow_html=True)


# =========================================================
# 2. ULTRA-PREMIUM MODERN OBSIDIAN GLASS THEME
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

/* Background Atmosphere - Slick Obsidian Canvas with Multi-Orb Lighting */
[data-testid="stAppViewContainer"] {
    background: 
        radial-gradient(circle at 12% 10%, rgba(99, 102, 241, 0.18) 0%, transparent 45%),
        radial-gradient(circle at 88% 80%, rgba(168, 85, 247, 0.16) 0%, transparent 45%),
        radial-gradient(circle at 50% 45%, rgba(14, 165, 233, 0.09) 0%, transparent 55%),
        #07090e !important;
    color: #f1f5f9 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}

[data-testid="stSidebar"] {
    background: rgba(10, 14, 23, 0.94) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
    backdrop-filter: blur(25px);
}

.block-container {
    max-width: 1180px !important;
    padding-top: 1.5rem !important;
    padding-bottom: 3.5rem !important;
}

header[data-testid="stHeader"] {
    background: transparent !important;
}

/* Typography Overrides */
[data-testid="stMetricValue"] {
    color: #f8fafc !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 800 !important;
}

[data-testid="stMetricLabel"] {
    color: #94a3b8 !important;
    font-weight: 600 !important;
    font-size: 13px !important;
}

[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3,
[data-testid="stMarkdownContainer"] h4 {
    color: #f8fafc !important;
    font-family: 'Outfit', sans-serif !important;
}

[data-testid="stWidgetLabel"] label,
[data-testid="stWidgetLabel"] p {
    color: #cbd5e1 !important;
    font-weight: 600 !important;
}

/* Sidebar Brand Header */
.sidebar-brand {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 6px 0 18px 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    margin-bottom: 20px;
}

.brand-icon {
    font-size: 28px;
    width: 52px;
    height: 52px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.35), rgba(168, 85, 247, 0.35));
    border: 1px solid rgba(99, 102, 241, 0.5);
    border-radius: 16px;
    box-shadow: 0 8px 25px rgba(99, 102, 241, 0.3);
}

.brand-title {
    font-family: 'Outfit', sans-serif;
    font-size: 21px;
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

/* Sidebar Cards */
.side-card {
    background: rgba(17, 24, 39, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 14px;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
}

.side-label {
    font-size: 11px;
    font-weight: 700;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    margin-bottom: 6px;
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
    width: 9px;
    height: 9px;
    border-radius: 50%;
    background: #10b981;
    box-shadow: 0 0 12px #10b981;
    display: inline-block;
    animation: pulseDot 2s infinite ease-in-out;
}

@keyframes pulseDot {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.6; transform: scale(1.2); }
}

.arch-tag {
    display: inline-block;
    background: rgba(99, 102, 241, 0.16);
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
    padding: 10px 10px 24px 10px;
}

.badge-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(168, 85, 247, 0.2));
    border: 1px solid rgba(99, 102, 241, 0.45);
    color: #c7d2fe;
    font-size: 12px;
    font-weight: 700;
    padding: 7px 20px;
    border-radius: 9999px;
    margin-bottom: 14px;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    box-shadow: 0 0 25px rgba(99, 102, 241, 0.25);
}

.hero-h1 {
    font-family: 'Outfit', sans-serif;
    font-size: 52px;
    font-weight: 900;
    letter-spacing: -1.4px;
    background: linear-gradient(135deg, #ffffff 20%, #cbd5e1 45%, #818cf8 75%, #c084fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    line-height: 1.15;
    filter: drop-shadow(0 4px 25px rgba(99, 102, 241, 0.3));
}

.hero-p {
    font-size: 16px;
    color: #94a3b8;
    max-width: 650px;
    margin: 12px auto 0 auto;
    line-height: 1.6;
}

/* Image preview styling */
[data-testid="stImage"] img {
    border-radius: 20px !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7) !important;
    transition: transform 0.3s ease;
}

[data-testid="stImage"] img:hover {
    transform: scale(1.01);
}

/* File Uploader styling */
[data-testid="stFileUploaderDropzone"] {
    background: rgba(17, 24, 39, 0.55) !important;
    border: 2px dashed rgba(99, 102, 241, 0.4) !important;
    border-radius: 20px !important;
    padding: 24px 20px !important;
    transition: all 0.25s ease !important;
}

[data-testid="stFileUploaderDropzone"]:hover {
    border-color: rgba(168, 85, 247, 0.75) !important;
    background: rgba(17, 24, 39, 0.85) !important;
    box-shadow: 0 0 30px rgba(99, 102, 241, 0.2) !important;
}

/* Glass Card */
.glass-box {
    background: rgba(17, 24, 39, 0.65);
    border: 1px solid rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(20px);
    border-radius: 22px;
    padding: 24px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.45);
}

/* Verdict Banners */
.result-banner-cat {
    background: linear-gradient(135deg, rgba(244, 63, 94, 0.22) 0%, rgba(217, 70, 239, 0.12) 100%);
    border: 2px solid rgba(244, 63, 94, 0.6);
    border-radius: 22px;
    padding: 24px;
    text-align: center;
    box-shadow: 0 16px 45px -5px rgba(244, 63, 94, 0.35);
    margin-bottom: 20px;
    animation: fadeIn 0.4s ease-out;
}

.result-banner-dog {
    background: linear-gradient(135deg, rgba(14, 165, 233, 0.22) 0%, rgba(99, 102, 241, 0.12) 100%);
    border: 2px solid rgba(56, 189, 248, 0.6);
    border-radius: 22px;
    padding: 24px;
    text-align: center;
    box-shadow: 0 16px 45px -5px rgba(56, 189, 248, 0.35);
    margin-bottom: 20px;
    animation: fadeIn 0.4s ease-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
}

.result-avatar {
    font-size: 68px;
    margin-bottom: 6px;
    filter: drop-shadow(0 8px 18px rgba(0, 0, 0, 0.45));
}

.result-name {
    font-family: 'Outfit', sans-serif;
    font-size: 36px;
    font-weight: 900;
    color: #ffffff;
    margin-bottom: 6px;
    letter-spacing: -0.5px;
}

.conf-badge {
    display: inline-block;
    padding: 7px 22px;
    border-radius: 9999px;
    background: rgba(0, 0, 0, 0.5);
    border: 1px solid rgba(255, 255, 255, 0.18);
    font-size: 15px;
    font-weight: 700;
    color: #ffffff;
    font-family: 'JetBrains Mono', monospace;
}

/* Custom Probability Bars */
.prob-card {
    background: rgba(13, 18, 30, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 12px;
}

.prob-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
}

.prob-title {
    font-weight: 700;
    font-size: 15px;
    color: #f8fafc;
    display: flex;
    align-items: center;
    gap: 8px;
}

.prob-val {
    font-family: 'JetBrains Mono', monospace;
    font-size: 16px;
    font-weight: 700;
}

.prob-bar-bg {
    width: 100%;
    height: 10px;
    background: rgba(255, 255, 255, 0.08);
    border-radius: 9999px;
    overflow: hidden;
}

.prob-bar-fill-cat {
    height: 100%;
    background: linear-gradient(90deg, #f43f5e, #fb7185);
    border-radius: 9999px;
    box-shadow: 0 0 14px rgba(244, 63, 94, 0.7);
    transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}

.prob-bar-fill-dog {
    height: 100%;
    background: linear-gradient(90deg, #0284c7, #38bdf8);
    border-radius: 9999px;
    box-shadow: 0 0 14px rgba(56, 189, 248, 0.7);
    transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Buttons */
.stButton > button {
    width: 100% !important;
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #d946ef 100%) !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    padding: 12px 24px !important;
    border-radius: 14px !important;
    border: none !important;
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.35) !important;
    transition: all 0.2s ease !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 12px 30px rgba(168, 85, 247, 0.55) !important;
}

/* Tabs Styling */
[data-testid="stTabs"] [role="tablist"] {
    gap: 8px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    padding-bottom: 8px;
}

[data-testid="stTabs"] button[role="tab"] {
    background: rgba(17, 24, 39, 0.6) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 12px !important;
    color: #94a3b8 !important;
    font-weight: 600 !important;
    padding: 8px 18px !important;
}

[data-testid="stTabs"] button[role="tab"][aria-selected="true"] {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.25), rgba(168, 85, 247, 0.25)) !important;
    border-color: rgba(99, 102, 241, 0.6) !important;
    color: #ffffff !important;
    box-shadow: 0 4px 15px rgba(99, 102, 241, 0.25);
}

/* Footer */
.footer-text {
    text-align: center;
    color: #64748b;
    font-size: 13px;
    padding: 35px 0 10px 0;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
    margin-top: 45px;
}
</style>
""")


# =========================================================
# 3. DEVICE & MODEL SETUP
# =========================================================

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
device_name = "NVIDIA CUDA GPU ⚡" if torch.cuda.is_available() else "CPU 💻"


@st.cache_resource
def load_model():
    candidate_paths = [
        Path("models/cat_dog_cnn.pth"),
        Path("../models/cat_dog_cnn.pth"),
        Path(__file__).resolve().parent.parent / "models" / "cat_dog_cnn.pth",
        Path(__file__).resolve().parent / "models" / "cat_dog_cnn.pth",
    ]
    path_to_load = next((p for p in candidate_paths if p.exists()), None)

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
# 4. ENHANCED SIDEBAR CONTROLS
# =========================================================

with st.sidebar:
    render_html("""
    <div class="sidebar-brand">
        <div class="brand-icon">🐾</div>
        <div>
            <div class="brand-title">VisionAI</div>
            <div class="brand-badge">Neural Classifier</div>
        </div>
    </div>
    """)

    # Model Status
    status_dot = '<span class="live-dot"></span>' if model is not None else '<span style="color:#ef4444;">●</span>'
    status_text = "Model Active & Ready" if model is not None else "Weights Missing"

    render_html(f"""
    <div class="side-card">
        <div class="side-label">System Status</div>
        <div class="side-val">{status_dot} {status_text}</div>
        <div style="margin-top: 8px; font-size: 12px; color: #94a3b8;">
            Compute: <strong style="color: #c7d2fe;">{device_name}</strong>
        </div>
    </div>
    """)

    # Architecture Overview
    render_html("""
    <div class="side-card">
        <div class="side-label">Network Specs</div>
        <div style="font-weight: 700; font-size: 14px; margin-bottom: 8px; color: #f8fafc;">
            CatDogCNN (2-Block)
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
        <div class="side-label" style="color: #a5b4fc;">💡 Pro Tips</div>
        <div style="font-size: 12px; color: #cbd5e1; line-height: 1.6; margin-top: 4px;">
            • High-contrast pet faces yield >98% confidence<br>
            • Standard input size: 224×224 RGB<br>
            • Supports JPG, PNG, WEBP formats
        </div>
    </div>
    """)


# =========================================================
# 5. HERO SECTION
# =========================================================

render_html("""
<div class="hero-box">
    <div class="badge-pill">
        <span>⚡ Deep Learning · PyTorch CNN</span>
    </div>
    <h1 class="hero-h1">VisionAI · Cat vs Dog Classifier</h1>
    <p class="hero-p">
        Upload or choose a pet picture to identify whether it's a <strong>Cat 🐱</strong> or a <strong>Dog 🐶</strong>
        with instant neural feature extraction and confidence analysis.
    </p>
</div>
""")


# =========================================================
# 6. MODEL CHECK
# =========================================================

if model is None:
    st.error("⚠️ **Model Weights Missing!** Could not locate `models/cat_dog_cnn.pth`.")
    st.info("Please train the model first by running:\n```bash\npython src/train.py\n```")
    st.stop()


# =========================================================
# 7. IMAGE TRANSFORMATION PIPELINE
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
# 8. TABS INTERFACE
# =========================================================

tab_infer, tab_arch, tab_dataset = st.tabs([
    "🔮 Instant Classifier",
    "🧬 Neural Architecture",
    "📚 Dataset & Pipeline"
])

with tab_infer:
    # Quick Sample Buttons
    cat_sample_path = Path("data/test/Cat/10001.jpg")
    dog_sample_path = Path("data/test/Dog/0.jpg")

    # If samples don't exist at relative path, try resolving parent
    if not cat_sample_path.exists():
        cat_sample_path = Path("../data/test/Cat/10001.jpg")
    if not dog_sample_path.exists():
        dog_sample_path = Path("../data/test/Dog/0.jpg")

    has_samples = cat_sample_path.exists() and dog_sample_path.exists()

    selected_image = None

    if has_samples:
        st.markdown("<p style='font-size:13px; font-weight:700; color:#94a3b8; margin-bottom:6px;'>⚡ QUICK TEST SAMPLES</p>", unsafe_allow_html=True)
        col_s1, col_s2, col_s3 = st.columns([1, 1, 2])
        with col_s1:
            if st.button("🐱 Load Cat Sample", use_container_width=True):
                st.session_state["demo_sample"] = "cat"
        with col_s2:
            if st.button("🐶 Load Dog Sample", use_container_width=True):
                st.session_state["demo_sample"] = "dog"
        with col_s3:
            if st.session_state.get("demo_sample"):
                if st.button("🔄 Clear Sample", use_container_width=True):
                    st.session_state["demo_sample"] = None
                    st.rerun()

    uploaded_file = st.file_uploader(
        "Upload a Pet Image (JPG, PNG, WEBP)",
        type=["jpg", "jpeg", "png", "webp"],
        help="Upload a clear pet photo to analyze."
    )

    if uploaded_file is not None:
        raw_img = Image.open(uploaded_file)
        selected_image = raw_img.convert("RGB") if raw_img.mode != "RGB" else raw_img
    elif st.session_state.get("demo_sample") == "cat" and cat_sample_path.exists():
        raw_img = Image.open(cat_sample_path)
        selected_image = raw_img.convert("RGB")
    elif st.session_state.get("demo_sample") == "dog" and dog_sample_path.exists():
        raw_img = Image.open(dog_sample_path)
        selected_image = raw_img.convert("RGB")

    # Results Section
    if selected_image is not None:
        render_html("<div style='margin-top: 20px;'></div>")
        col_img, col_result = st.columns([1, 1.15], gap="large")

        with col_img:
            st.markdown("#### 📷 Image Preview")
            st.image(selected_image, use_container_width=True)

            col_res, col_chan = st.columns(2)
            with col_res:
                st.metric(label="📐 Resolution", value=f"{selected_image.width} × {selected_image.height}")
            with col_chan:
                st.metric(label="🎨 Format", value="RGB (3-Ch)")

        with col_result:
            st.markdown("#### 🤖 AI Classification")

            should_predict = True
            if not auto_predict:
                should_predict = st.button("🔍 Run Prediction", key="manual_btn")

            if should_predict:
                start_clock = time.perf_counter()
                with st.spinner("Analyzing neural features..."):
                    img_tensor = transform(selected_image).unsqueeze(0).to(device)

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
                        st.toast(f"🎯 High Match Identified: {prediction} ({confidence_pct:.1f}%)", icon="✨")

                    # Verdict Banner
                    render_html(f"""
                    <div class="{banner_cls}">
                        <div class="result-avatar">{emoji_icon}</div>
                        <div class="result-name">{prediction} Detected</div>
                        <div class="conf-badge">
                            Confidence: <strong style="color: {color_accent};">{confidence_pct:.2f}%</strong>
                        </div>
                    </div>
                    """)

                    # Custom Glowing Probability Bars
                    if show_distribution:
                        st.markdown("#### 📊 Probability Breakdown")

                        render_html(f"""
                        <div class="prob-card">
                            <div class="prob-header">
                                <span class="prob-title">🐱 Cat</span>
                                <span class="prob-val" style="color: #fb7185;">{cat_prob_pct:.1f}%</span>
                            </div>
                            <div class="prob-bar-bg">
                                <div class="prob-bar-fill-cat" style="width: {cat_prob_pct:.1f}%;"></div>
                            </div>
                        </div>

                        <div class="prob-card">
                            <div class="prob-header">
                                <span class="prob-title">🐶 Dog</span>
                                <span class="prob-val" style="color: #38bdf8;">{dog_prob_pct:.1f}%</span>
                            </div>
                            <div class="prob-bar-bg">
                                <div class="prob-bar-fill-dog" style="width: {dog_prob_pct:.1f}%;"></div>
                            </div>
                        </div>
                        """)

                    # Telemetry Metrics
                    col_lat, col_eng = st.columns(2)
                    with col_lat:
                        st.metric(label="⏱️ Inference Latency", value=f"{latency_ms:.1f} ms")
                    with col_eng:
                        st.metric(label="⚙️ Compute Engine", value=device.type.upper())

    else:
        # Empty Placeholder
        render_html("""
        <div class="glass-box" style="text-align: center; padding: 50px 20px; margin-top: 25px;">
            <div style="font-size: 55px; margin-bottom: 12px;">🐾</div>
            <div style="font-family: 'Outfit'; font-size: 23px; font-weight: 800; color: #ffffff;">No Image Selected</div>
            <div style="font-size: 14px; color: #94a3b8; margin-top: 8px; max-width: 440px; margin-left: auto; margin-right: auto; line-height: 1.6;">
                Upload your cat or dog image above, or click one of the quick test buttons to run real-time inference.
            </div>
        </div>
        """)

with tab_arch:
    render_html("""
    <div class="glass-box" style="margin-top: 15px;">
        <h3 style="margin-top: 0; color: #ffffff;">🧬 CatDogCNN Architecture</h3>
        <p style="color: #94a3b8; font-size: 14px; line-height: 1.6;">
            A custom convolutional neural network designed for binary classification with spatial feature downsampling and dense classification.
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-top: 20px;">
            <div class="side-card" style="margin: 0;">
                <div class="side-label">Input Layer</div>
                <div style="font-weight: 700; color: #ffffff; font-size: 15px;">3 × 224 × 224</div>
                <div style="color: #94a3b8; font-size: 12px; margin-top: 4px;">Normalized RGB Channels</div>
            </div>

            <div class="side-card" style="margin: 0;">
                <div class="side-label">Conv Block 1</div>
                <div style="font-weight: 700; color: #ffffff; font-size: 15px;">Conv2D(3, 32) + MaxPool</div>
                <div style="color: #94a3b8; font-size: 12px; margin-top: 4px;">Output: 32 × 112 × 112</div>
            </div>

            <div class="side-card" style="margin: 0;">
                <div class="side-label">Conv Block 2</div>
                <div style="font-weight: 700; color: #ffffff; font-size: 15px;">Conv2D(32, 64) + MaxPool</div>
                <div style="color: #94a3b8; font-size: 12px; margin-top: 4px;">Output: 64 × 56 × 56</div>
            </div>

            <div class="side-card" style="margin: 0;">
                <div class="side-label">Dense Classifier</div>
                <div style="font-weight: 700; color: #ffffff; font-size: 15px;">Linear(200704, 128) ➔ 2</div>
                <div style="color: #94a3b8; font-size: 12px; margin-top: 4px;">Binary Logits Output</div>
            </div>
        </div>
    </div>
    """)

with tab_dataset:
    render_html("""
    <div class="glass-box" style="margin-top: 15px;">
        <h3 style="margin-top: 0; color: #ffffff;">📚 Data Processing & Pipeline</h3>
        <p style="color: #94a3b8; font-size: 14px; line-height: 1.6;">
            The dataset uses Microsoft's Cats and Dogs dataset with stratified 70/15/15 splitting and PyTorch image augmentations.
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; margin-top: 20px;">
            <div class="side-card" style="margin: 0;">
                <div class="side-label">Data Cleaning</div>
                <div style="font-weight: 700; color: #ffffff; font-size: 14px;">clean_images.py</div>
                <div style="color: #94a3b8; font-size: 12px; margin-top: 4px;">Scans images with PIL to remove corrupted and truncated files.</div>
            </div>

            <div class="side-card" style="margin: 0;">
                <div class="side-label">Splitting Pipeline</div>
                <div style="font-weight: 700; color: #ffffff; font-size: 14px;">split_dataset.py</div>
                <div style="color: #94a3b8; font-size: 12px; margin-top: 4px;">70% Train, 15% Validation, 15% Test with seed=42 reproducibility.</div>
            </div>

            <div class="side-card" style="margin: 0;">
                <div class="side-label">Augmentations</div>
                <div style="font-weight: 700; color: #ffffff; font-size: 14px;">torchvision.transforms</div>
                <div style="color: #94a3b8; font-size: 12px; margin-top: 4px;">RandomHorizontalFlip, RandomRotation(10), ImageNet normalization.</div>
            </div>
        </div>
    </div>
    """)


# =========================================================
# 9. FOOTER
# =========================================================

render_html("""
<div class="footer-text">
    Crafted with ❤️ using <strong>PyTorch</strong> & <strong>Streamlit</strong> · VisionAI Neural Classifier
</div>
""")