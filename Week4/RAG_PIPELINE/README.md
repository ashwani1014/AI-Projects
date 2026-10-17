# 📚 RAG Pipeline (Retrieval-Augmented Generation)

An end-to-end Retrieval-Augmented Generation (RAG) system architecture designed to ingest unstructured documents (PDFs), chunk and index context, and provide grounded contextual generation.

---

## 🏗️ Architecture & Workflow

```text
[ Raw PDF Documents ]
         │
         ▼
[ Ingestion & Text Extraction (PyMuPDF) ]
         │
         ▼
[ Context-Aware Chunking (Overlap Strategy) ]
         │
         ▼
[ Embedding Generation & Vector Store (ChromaDB / FAISS) ] ── (In-Progress)
         │
         ▼
[ Semantic Retrieval & Top-K Reranking ] ──────────────── (In-Progress)
         │
         ▼
[ Grounded LLM Response Generation ] ──────────────────── (In-Progress)
```

---

## 📂 Project Structure

```text
RAG_PIPELINE/
├── Backend/
│   ├── ingestion.py      # PDF text extraction (PyMuPDF) & sliding-window chunking
│   ├── retrieval.py      # Semantic vector search & context retrieval
│   ├── generation.py     # Prompt formatting & LLM answer generation
│   └── main.py           # Backend entrypoint / API endpoints
├── Frontend/
│   └── frontend/         # React + Vite interactive dashboard
│       ├── src/
│       ├── package.json
│       └── vite.config.js
├── data/                 # Raw PDF storage directory (git-ignored)
├── requirements.txt      # Python dependencies
└── README.md
```

---

## ⚙️ Ingestion & Chunking Strategy

### 1. Text Extraction (`Backend/ingestion.py`)
- Uses **PyMuPDF (`fitz`)** for high-performance and reliable text parsing across multi-page PDF documents.
- Annotates pages with page markers `[Page X]` to retain citation metadata during retrieval.

### 2. Sliding Window Chunking
- **Default Chunk Size:** 800 characters
- **Overlap Window:** 120 characters
- **Objective:** Prevents critical semantic boundaries (like sentences or code snippets) from being severed across chunk edges, maintaining coherent context for embeddings.

---

## 🚀 Getting Started

### 1. Python Environment Setup
```bash
# Navigate to RAG Pipeline
cd Week4/RAG_PIPELINE

# Create and activate virtual environment
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Frontend Setup (React + Vite)
```bash
cd Frontend/frontend
npm install
npm run dev
```

---

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Document Ingestion:** PyMuPDF (`fitz`)
- **Frontend:** React 19, Vite, Modern CSS