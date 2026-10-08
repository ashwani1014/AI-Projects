# 🐾 Cat vs Dog Neural Classifier (VisionAI)

An end-to-end Computer Vision binary classification system built with **PyTorch** and deployed with a modern **Streamlit** obsidian glassmorphism web interface.

---

## 📌 Project Overview

- **Problem Type:** Binary Image Classification (Cat vs. Dog)
- **Deep Learning Framework:** PyTorch & Torchvision
- **Neural Network Architecture:** Custom `CatDogCNN` (2 Convolutional Blocks + Fully Connected Classifier Head)
- **Loss Function:** `CrossEntropyLoss`
- **Optimizer:** `Adam` (lr=0.001)
- **User Interface:** Streamlit with customized obsidian dark glassmorphism styling, live image preview, and real-time softmax confidence scoring.

---

## 🧠 Model Architecture (`CatDogCNN`)

```text
Input Image (3 x 224 x 224)
   │
   ▼
[Conv2d (3 -> 32, kernel=3, padding=1) + ReLU + MaxPool2d(2)]  ➔ (32 x 112 x 112)
   │
   ▼
[Conv2d (32 -> 64, kernel=3, padding=1) + ReLU + MaxPool2d(2)] ➔ (64 x 56 x 56)
   │
   ▼
[Flatten]                                                      ➔ (200,704 features)
   │
   ▼
[Linear (200704 -> 128) + ReLU]
   │
   ▼
[Linear (128 -> 2)]                                            ➔ Logits [Cat, Dog]
```

---

## 🔄 Data Pipeline & Augmentations

- **Integrity Verification (`clean_images.py` & `image.py`):** Scans and validates image files with PIL to detect and eliminate corrupted/truncated images.
- **Dataset Splitting (`split_dataset.py`):** Splits data into **70% Train**, **15% Validation**, and **15% Test** partitions with reproducible random seeding.
- **Data Augmentation (`dataset.py`):**
  - **Train:** Resizing to 224x224, `RandomHorizontalFlip()`, `RandomRotation(10)`, Conversion to Tensor, and ImageNet Normalization (`mean=[0.485, 0.456, 0.406]`, `std=[0.229, 0.224, 0.225]`).
  - **Val / Test / Inference:** Resizing to 224x224, Conversion to Tensor, and ImageNet Normalization.

---

## 📁 Project Structure

```text
Cat_Dog_Classifier/
├── data/                         # Train, validation, and test datasets (excluded from git)
├── models/                       # Serialized PyTorch model weights (.pth) (excluded from git)
├── src/
│   ├── app.py                    # Streamlit web application with modern obsidian UI
│   ├── dataset.py                # Torchvision transformations and DataLoader setup
│   ├── image.py                  # Image file verification helper
│   ├── model.py                  # PyTorch CatDogCNN model definition
│   ├── split_dataset.py          # Train / Val / Test dataset splitter
│   ├── test.py                   # Model evaluation and test accuracy measurement
│   └── train.py                  # Training loop with loss and accuracy tracking
├── clean_images.py               # Corrupted image detection and cleaning script
├── requirements.txt              # Project dependencies
└── README.md                     # Documentation
```

---

## 🚀 How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Verify and Split the Dataset
```bash
python clean_images.py
python src/split_dataset.py
```

### 3. Train the CNN Model
```bash
python src/train.py
```
*Trained weights will be saved to `models/cat_dog_cnn.pth`.*

### 4. Evaluate Model on Test Set
```bash
python src/test.py
```

### 5. Launch the Streamlit Web Application
```bash
streamlit run src/app.py
```
