# 🤖 AI & Machine Learning Engineering Journey

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)](https://nextjs.org/)
[![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Express.js](https://img.shields.io/badge/Express.js-000000?style=for-the-badge&logo=express&logoColor=white)](https://expressjs.com/)
[![Groq](https://img.shields.io/badge/Groq%20Cloud-F55036?style=for-the-badge&logo=fastapi&logoColor=white)](https://groq.com/)

> A structured, hands-on repository documenting my 30-day intensive journey from **Data Science and Classical Machine Learning** to **Deep Learning, Computer Vision, RAG Pipelines, and Full-Stack GenAI Applications**.

---

## 📌 Philosophy & Learning Methodology

- **Goal:** Build rock-solid AI fundamentals + Classical Machine Learning + Deep Learning/CNNs + GenAI/RAG + a deployable full-stack AI production project.
- **Recommended Pace:** 2–5 focused hours/day
- **Effort Allocation:** 📖 **40% Theory** • 💻 **40% Coding** • 🚀 **20% Projects**

---

## 📅 30-Day Intensive AI Engineering Roadmap

Below is the complete 30-day curriculum followed to master the core domains of AI Engineering and build the projects housed in this repository:

<details open>
<summary><b>🗓️ Week 1: AI Foundations, Math & Exploratory Data Analysis (Days 1–7)</b></summary>

| Day | Topic | What Was Learned | Daily Hands-On Task | Deliverable / Artifact | Est. Time |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **Day 1** | AI Foundations | AI vs ML vs DL vs GenAI; industry applications; role of an AI engineer | Watch introductory lectures & create structured notes | AI Landscape Map | 2.0h |
| **Day 2** | Python for AI | NumPy basics, n-dim arrays, indexing, slicing, vectorization | Code 15 core NumPy tensor operations | NumPy Practice Notebook | 2.5h |
| **Day 3** | Python for AI | Pandas: Series, DataFrames, filtering, aggregation, `groupby` | Analyze and summarize real-world tabular data | Data Analysis Notebook | 2.5h |
| **Day 4** | Math for AI | Linear Algebra: Vectors, matrices, dot products, vector/matrix norms | Implement core algebraic transformations with NumPy | Math Cheat Sheet | 2.0h |
| **Day 5** | Math for AI | Probability distributions, mean, variance, standard deviation | Solve 15 applied probability and statistical problems | Probability Notes | 2.0h |
| **Day 6** | Data & Visualization | Matplotlib & Seaborn, data cleaning, missing value strategies, IQR outliers | Clean, impute, and visualize messy datasets | Comprehensive EDA Notebook | 2.5h |
| **Day 7** | **Weekly Project** | End-to-end Exploratory Data Analysis on real-estate dataset | Clean data, detect outliers, perform correlation analysis & document findings | [Mini Project 1: Ames Housing EDA](file:///e:/JULY_PLAN/AI/AI-Projects/Week1/EDA_Project.ipynb) | 3.0h |

</details>

<details open>
<summary><b>🗓️ Week 2: Supervised Machine Learning & Production Pipelines (Days 8–14)</b></summary>

| Day | Topic | What Was Learned | Daily Hands-On Task | Deliverable / Artifact | Est. Time |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **Day 8** | Machine Learning | Supervised vs. unsupervised; feature matrices, labels; train/test splits | Build first Scikit-Learn baseline model | ML Basics Notebook | 2.5h |
| **Day 9** | ML Algorithms | Linear regression mathematics, cost functions, evaluation metrics (MSE, RMSE, R²) | Implement, evaluate, and interpret regression models | [Regression Notebook](file:///e:/JULY_PLAN/AI/AI-Projects/Week2/Machine_Learning_House_Price_Prediction.ipynb) | 2.5h |
| **Day 10** | ML Algorithms | Logistic regression, sigmoid activation, classification metrics (Precision, Recall, F1) | Train binary classifier & analyze confusion matrix | Classification Notebook | 2.5h |
| **Day 11** | ML Algorithms | Non-linear models: Decision Trees, Random Forests, feature importances | Compare linear vs. tree-based ensemble estimators | Tree Models Comparison | 2.5h |
| **Day 12** | ML Algorithms | K-Nearest Neighbors (KNN), Support Vector Machines (SVM); feature scaling (`StandardScaler`) | Compare KNN and SVM performance across scaled inputs | Model Comparison Benchmark | 2.5h |
| **Day 13** | ML Practice | $K$-Fold cross-validation, bias-variance tradeoff, Scikit-Learn `Pipeline`, `GridSearchCV` | Build automated ML pipeline & hyperparameter search | [Tuned Model with CV](file:///e:/JULY_PLAN/AI/AI-Projects/Week2/Tune_with_CV.ipynb) | 3.0h |
| **Day 14** | **Weekly Project** | End-to-End Machine Learning System & Local Deployment | Train model, serialize pipeline (`.pkl`), build interactive web interface with Streamlit | [Mini Project 2: Student Attendance Predictor](file:///e:/JULY_PLAN/AI/AI-Projects/Week2/Attendance_Project/app.py) | 4.0h |

</details>

<details open>
<summary><b>🗓️ Week 3: Deep Learning, PyTorch & Computer Vision (Days 15–21)</b></summary>

| Day | Topic | What Was Learned | Daily Hands-On Task | Deliverable / Artifact | Est. Time |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **Day 15** | Deep Learning | Artificial Neural Networks, artificial neurons, activation functions (ReLU, Sigmoid), loss functions | Construct simple feedforward network conceptually | Neural Network Architecture Notes | 2.5h |
| **Day 16** | PyTorch Fundamentals | PyTorch tensors, autograd, GPU acceleration (`cuda`), custom `Dataset` & `DataLoader` | Implement custom tensor transformations & batching | PyTorch Tensor Notebook | 2.5h |
| **Day 17** | PyTorch Mechanics | Complete training loop: forward pass, loss calculation (`CrossEntropyLoss`), backprop, optimizer (`Adam`) | Train small PyTorch classifier from scratch | Training Loop Implementation | 3.0h |
| **Day 18** | Computer Vision | Convolutional Neural Networks (CNNs), kernel filters, spatial feature maps, pooling | Build multi-layer convolutional neural network | CNN Feature Extraction Notebook | 3.0h |
| **Day 19** | NLP Foundations | Text tokenization, subwords (BPE), word embeddings, cosine similarity, self-attention intuition | Explore tokenizers and embedding distance spaces | NLP & Embeddings Exploration | 3.0h |
| **Day 20** | Transformers | Transformer architecture: Multi-Head Attention, positional encodings, Encoder/Decoder heads | Deconstruct transformer blocks & query/key/value mechanics | Transformer Mechanics Notes | 3.0h |
| **Day 21** | **Weekly Project** | Full Deep Learning Computer Vision Classifier | Train CNN on Cat vs Dog dataset, evaluate accuracy, serialize weights (`.pth`), build Streamlit UI | [Mini Project 3: VisionAI Classifier](file:///e:/JULY_PLAN/AI/AI-Projects/Week3/Cat_Dog_Classifier/src/app.py) | 4.0h |

</details>

<details open>
<summary><b>🗓️ Week 4: Generative AI, RAG Pipelines & Agent Tooling (Days 22–28)</b></summary>

| Day | Topic | What Was Learned | Daily Hands-On Task | Deliverable / Artifact | Est. Time |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **Day 22** | Generative AI | Large Language Models (LLMs), token budgets, context windows, sampling & greedy decoding | Compare open vs. proprietary LLM paradigms | LLM Architectural Notes | 2.5h |
| **Day 23** | Prompt Engineering | Zero-shot, few-shot prompting, system personas, structured outputs (JSON schema), guardrails | Design comprehensive prompt suite for specialized personas | Prompt Engineering Library | 2.0h |
| **Day 24** | LLM APIs | API integration, multi-turn messages schema, temperature tuning, streaming responses | Build programmatic script calling cloud inference APIs | Cloud LLM API Client | 3.0h |
| **Day 25** | Embeddings & Vector DBs | Dense vector embeddings, chunking strategies (chunk size + overlap), vector similarity indexing | Ingest documents and run semantic similarity searches | Semantic Search Prototype | 3.0h |
| **Day 26** | RAG Architecture | Retrieval-Augmented Generation, document grounding, context injection, prompt stitching | Build PDF text parser & sliding-window chunker with PyMuPDF | [RAG Ingestion Engine](file:///e:/JULY_PLAN/AI/AI-Projects/Week4/RAG_PIPELINE/Backend/ingestion.py) | 4.0h |
| **Day 27** | Agents & Tools | Autonomous agent loops, function/tool calling, reasoning traces, conversational guardrails | Construct structured tool-dispatching assistant logic | Agent Prototype Logic | 4.0h |
| **Day 28** | AI Engineering | Exposing AI microservices, REST APIs with Express/FastAPI, error boundaries, evaluation metrics | Build API server connecting frontend client to AI engine | Decoupled AI Backend Service | 4.0h |

</details>

<details open>
<summary><b>🗓️ Week 5: Capstone Project — Production Full-Stack AI Assistant (Days 29–30)</b></summary>

| Day | Topic | What Was Learned | Daily Hands-On Task | Deliverable / Artifact | Est. Time |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **Day 29** | Full-Stack Capstone | Decoupled full-stack architecture: Next.js (React 19, TypeScript, Tailwind) + Express.js + Groq SDK | Build production-ready interactive AI web app with conversational memory & tutoring personas | [Capstone MVP: Python Tutor Chatbot](file:///e:/JULY_PLAN/AI/AI-Projects/Week5/Pyhton%20Chatbot/) | 5.0h |
| **Day 30** | Deployment & Portfolio | Environment security (`.env.example`), production build testing, Git hygiene, technical documentation | Finalize repository README, clean commit history, prepare portfolio showcase | Production Repository & Portfolio | 5.0h |

</details>

---

## 🏆 Featured Project Highlights

### 1. 📊 Week 1 — Ames Housing Exploratory Data Analysis
- **Focus:** Data Wrangling, Descriptive Statistics & Visual Analytics
- **Techniques:** Missing value imputation, IQR outlier detection, distribution plots, Seaborn correlation heatmaps.
- **Artifact:** [`Week1/EDA_Project.ipynb`](file:///e:/JULY_PLAN/AI/AI-Projects/Week1/EDA_Project.ipynb)

---

### 2. ⚙️ Week 2 — Student Attendance & Performance Predictor
- **Focus:** Supervised Classification, Scikit-Learn Pipelines & Model Deployment
- **Architecture:** Feature Scaling ➔ Scikit-Learn `Pipeline` ➔ $K$-Fold Cross Validation ➔ `GridSearchCV` ➔ Model Serialization (`.pkl`) ➔ **Streamlit Web Application**.
- **Artifacts:**
  - Training & GridSearch: [`Week2/Attendance_Project/train.py`](file:///e:/JULY_PLAN/AI/AI-Projects/Week2/Attendance_Project/train.py)
  - Interactive Web App: [`Week2/Attendance_Project/app.py`](file:///e:/JULY_PLAN/AI/AI-Projects/Week2/Attendance_Project/app.py)

---

### 3. 🐾 Week 3 — VisionAI: Cat vs Dog PyTorch Neural Classifier
- **Focus:** Deep Learning, Convolutional Neural Networks (CNNs) & Computer Vision
- **Architecture:** 2 Convolutional Blocks (`Conv2d` + `ReLU` + `MaxPool2d`) + Fully Connected classification head (`Linear` + `ReLU` + `Linear`).
- **Pipeline:** Dataset validation ➔ Train/Val/Test splitting ➔ Data Augmentation (`torchvision.transforms`) ➔ Training loop with Adam optimizer & CrossEntropyLoss ➔ **Streamlit UI** with Obsidian dark glassmorphism styling and real-time Softmax confidence scores.
- **Artifacts:**
  - Neural Network Model: [`Week3/Cat_Dog_Classifier/src/model.py`](file:///e:/JULY_PLAN/AI/AI-Projects/Week3/Cat_Dog_Classifier/src/model.py)
  - Training Engine: [`Week3/Cat_Dog_Classifier/src/train.py`](file:///e:/JULY_PLAN/AI/AI-Projects/Week3/Cat_Dog_Classifier/src/train.py)
  - Streamlit Dashboard: [`Week3/Cat_Dog_Classifier/src/app.py`](file:///e:/JULY_PLAN/AI/AI-Projects/Week3/Cat_Dog_Classifier/src/app.py)

---

### 4. ⚡ Week 4 — Enterprise RAG Pipeline (Retrieval-Augmented Generation)
- **Focus:** Document Ingestion, Character-Level Chunking & Decoupled Frontend
- **Key Modules:**
  - **PDF Text Ingestion:** High-speed document parsing via **PyMuPDF (`fitz`)**, annotating extracted pages with page metadata tags `[Page X]`.
  - **Context-Aware Sliding Window Chunking:** 800-character chunking with 120-character overlapping windows to maintain semantic continuity across boundaries.
  - **Modern Web Dashboard:** React 19 + Vite dashboard for document uploads and query interaction.
- **Artifacts:**
  - Ingestion Engine: [`Week4/RAG_PIPELINE/Backend/ingestion.py`](file:///e:/JULY_PLAN/AI/AI-Projects/Week4/RAG_PIPELINE/Backend/ingestion.py)
  - Frontend Interface: [`Week4/RAG_PIPELINE/Frontend/frontend/`](file:///e:/JULY_PLAN/AI/AI-Projects/Week4/RAG_PIPELINE/Frontend/frontend/)

---

### 5. 💬 Week 5 (Capstone) — Full-Stack Python Tutor AI Assistant
- **Focus:** Production GenAI Web Application, Cloud LLM Inference & Conversational Memory
- **Features:**
  - **Specialized AI Persona:** Prompt-engineered to teach Python, debug code, and prepare learners for technical interviews with structured step-by-step answers.
  - **Multi-Turn Contextual Memory:** Preserves conversational turns and understands context-dependent follow-ups (e.g. *"give an example"*, *"explain that type"*).
  - **Ultra-Fast LLM Inference:** Powered by **Groq Cloud API** for lightning-fast token generation.
  - **Production Architecture:** Decoupled **Next.js 15 (TypeScript + Tailwind CSS)** frontend + **Node.js/Express** backend gateway with rate-safety and input validation.
- **Artifacts:**
  - Backend API Gateway: [`Week5/Pyhton Chatbot/backend/server.js`](file:///e:/JULY_PLAN/AI/AI-Projects/Week5/Pyhton%20Chatbot/backend/server.js)
  - Frontend Chatbot Application: [`Week5/Pyhton Chatbot/chatbot-app/`](file:///e:/JULY_PLAN/AI/AI-Projects/Week5/Pyhton%20Chatbot/chatbot-app/)

---

## 📂 Repository Directory Tree

```text
AI-Projects/
├── Week1/
│   ├── Ames_Housing_EDA.csv                       # Housing dataset
│   └── EDA_Project.ipynb                          # Data analysis & visualization notebook
│
├── Week2/
│   ├── Attendance_Project/                        # End-to-end ML classification application
│   │   ├── app.py                                 # Streamlit dashboard
│   │   ├── train.py                               # Pipeline training & GridSearchCV script
│   │   ├── requirement.txt                        # Project dependencies
│   │   └── README.MD                              # Application documentation
│   ├── Machine_Learning_House_Price_Prediction.ipynb
│   └── Tune_with_CV.ipynb
│
├── Week3/
│   ├── Cat_Dog_Classifier/                        # Deep Learning Computer Vision project
│   │   ├── src/
│   │   │   ├── app.py                             # Streamlit UI with confidence scores
│   │   │   ├── dataset.py                         # PyTorch Dataset & DataLoader
│   │   │   ├── model.py                           # 2-Block CNN Architecture
│   │   │   ├── train.py                           # Training loop with validation
│   │   │   ├── test.py                            # Model evaluation script
│   │   │   └── split_dataset.py                   # Train/Val/Test data splitter
│   │   ├── clean_images.py                        # Corrupt image validation script
│   │   ├── requirements.txt
│   │   └── README.md
│   └── README.md                                  # Week 3 Overview
│
├── Week4/
│   ├── RAG_PIPELINE/                              # Retrieval-Augmented Generation project
│   │   ├── Backend/
│   │   │   ├── ingestion.py                       # PDF parser & sliding-window chunker
│   │   │   ├── retrieval.py                       # Vector search & ranking module
│   │   │   ├── generation.py                      # Grounded LLM response module
│   │   │   └── main.py                            # Backend service API
│   │   ├── Frontend/
│   │   │   └── frontend/                          # React 19 + Vite dashboard
│   │   ├── .env.example
│   │   ├── requirements.txt
│   │   └── README.md
│   └── README.md                                  # Week 4 Overview
│
├── Week5/
│   ├── Pyhton Chatbot/                            # Full-Stack LLM Python Tutor (Capstone)
│   │   ├── backend/                               # Express.js API gateway
│   │   │   ├── server.js                          # Groq API integration & prompt engine
│   │   │   ├── package.json
│   │   │   ├── .env.example
│   │   │   └── README.md
│   │   ├── chatbot-app/                           # Next.js 15+ frontend
│   │   │   ├── src/app/                           # App router, components & layouts
│   │   │   ├── package.json
│   │   │   ├── .env.example
│   │   │   └── README.md
│   │   └── README.md
│   └── README.md                                  # Week 5 Overview
│
├── .gitignore                                     # Comprehensive exclusion rules
└── README.md                                      # Repository overview & 30-Day Roadmap
```

---

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/ashwani1014/AI-Projects.git
cd AI-Projects
```

### 2. Running Individual Projects

<details>
<summary><b>Running Week 2: Student Attendance Predictor</b></summary>

```bash
cd Week2/Attendance_Project
python -m venv .venv
source .venv/bin/activate  # Or .venv\Scripts\activate on Windows
pip install -r requirement.txt
streamlit run app.py
```
</details>

<details>
<summary><b>Running Week 3: Cat vs Dog Neural Classifier</b></summary>

```bash
cd Week3/Cat_Dog_Classifier
python -m venv venv
source venv/bin/activate  # Or venv\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run src/app.py
```
</details>

<details>
<summary><b>Running Week 4: RAG Pipeline Frontend</b></summary>

```bash
cd Week4/RAG_PIPELINE/Frontend/frontend
npm install
npm run dev
```
</details>

<details>
<summary><b>Running Week 5: Python Tutor AI Chatbot</b></summary>

**Backend Service:**
```bash
cd "Week5/Pyhton Chatbot/backend"
npm install
cp .env.example .env
# Edit .env and paste your GROQ_API_KEY
npm run dev
```

**Frontend Application:**
```bash
cd "Week5/Pyhton Chatbot/chatbot-app"
npm install
cp .env.example .env.local
npm run dev
```
Open [http://localhost:3000](http://localhost:3000) in your browser.
</details>

---

## 🛠️ Complete Tech Stack

| Domain | Technologies & Frameworks |
| :--- | :--- |
| **Languages** | Python 3.10+, TypeScript, JavaScript, SQL |
| **Data Science & EDA** | NumPy, Pandas, Scipy, Matplotlib, Seaborn |
| **Machine Learning** | Scikit-Learn, Joblib, Cross-Validation, GridSearchCV |
| **Deep Learning & CV** | PyTorch, Torchvision, Pillow (PIL), Convolutional Neural Networks |
| **Generative AI & LLMs** | Groq Cloud SDK, Prompt Engineering, PyMuPDF (`fitz`), RAG |
| **Web Frontend** | Next.js 15, React 19, Vite, Tailwind CSS, Lucide Icons |
| **Web Backend** | Express.js, Node.js, REST APIs, Streamlit |
| **DevOps & Tooling** | Git, GitHub, Virtualenv, npm |

---

## 🛡️ Security & Git Hygiene
- Secret keys and API tokens (`.env`, `.env.local`) are strictly excluded via [`.gitignore`](file:///e:/JULY_PLAN/AI/AI-Projects/.gitignore).
- Template configuration files (`.env.example`) are provided across all applications for immediate onboarding.
- Heavy binary caches, virtual environments (`venv/`), dependencies (`node_modules/`), and build artifacts (`.next/`) are clean and excluded.

---

## 👤 Author
**Ashwani**
- GitHub: [@ashwani1014](https://github.com/ashwani1014)
- Repository: [AI-Projects](https://github.com/ashwani1014/AI-Projects)
