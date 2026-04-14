# 📄 Resume Screening System (NLP Project)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![NLP](https://img.shields.io/badge/NLP-Resume%20Matching-green)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![ML](https://img.shields.io/badge/Machine%20Learning-Project-orange)

---

## 📌 Project Overview
The **Resume Screening System** is an AI-powered NLP application that automatically ranks resumes based on their similarity to a given Job Description (JD).

It reduces manual effort in recruitment by extracting skills and experience from resumes and matching them with job requirements using NLP techniques like **TF-IDF and semantic embeddings**.

---

## ❗ Problem Statement
Recruiters face challenges when screening large volumes of resumes:

- ⏳ Time-consuming manual evaluation  
- ⚖️ Human bias in selection  
- ❌ Difficulty in handling large datasets  
- 📉 Inconsistent evaluation criteria  

### ✔️ Solution
This system automates resume screening using NLP to:
- Analyze resumes
- Compare with Job Description
- Rank candidates based on relevance score

---

## 🔄 Workflow Diagram
            ┌────────────────────────┐
            │ Upload Resumes + JD   │
            └──────────┬─────────────┘
                       ↓
            ┌────────────────────────┐
            │ Text Extraction        │
            │ (PDF / DOCX parsing)   │
            └──────────┬─────────────┘
                       ↓
            ┌────────────────────────┐
            │ Text Preprocessing     │
            │ Cleaning, tokenizing   │
            └──────────┬─────────────┘
                       ↓
            ┌────────────────────────┐
            │ Feature Extraction     │
            │ TF-IDF / Embeddings    │
            └──────────┬─────────────┘
                       ↓
            ┌────────────────────────┐
            │ Cosine Similarity      │
            │ Calculation            │
            └──────────┬─────────────┘
                       ↓
            ┌────────────────────────┐
            │ Resume Ranking System  │
            └──────────┬─────────────┘
                       ↓
            ┌────────────────────────┐
            │ Final Shortlisted List │
            └────────────────────────┘
            
---

## 🧰 Tech Stack
- 🐍 Python  
- ⚡ Streamlit (Web UI)  
- 📊 Pandas, NumPy  
- 🤖 Scikit-learn  
- 🧠 NLP (TF-IDF, Cosine Similarity, Embeddings)  
- 📄 PyPDF2 / python-docx (Resume parsing)

---

## ✨ Features
- 📂 Upload multiple resumes (PDF/DOCX)
- 📝 Paste Job Description
- 🔍 Automatic text extraction from resumes
- 🧹 Clean and preprocess text data
- 📊 Rank resumes based on similarity score
- 🧠 TF-IDF & Embedding-based matching
- ⚡ Fast and interactive Streamlit interface
- 📉 Skill gap / missing skills detection

---

## ⚙️ How It Works (Step-by-Step)

1. User uploads resumes and enters Job Description  
2. System extracts text from uploaded resumes  
3. Text is cleaned (stopwords removal, tokenization, normalization)  
4. TF-IDF vectors or embeddings are generated  
5. Cosine similarity is calculated between JD and each resume  
6. Each resume gets a relevance score  
7. Resumes are ranked in descending order  
8. Top candidates are displayed to recruiter  

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/your-username/resume-screening-system.git

# Navigate into project folder
cd resume-screening-system

# Create virtual environment
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
Model Techniques Used
TF-IDF Vectorization
Cosine Similarity
Word Embeddings (optional upgrade)
Text Preprocessing (NLTK / spaCy)
🚀 Future Improvements
🔥 Replace TF-IDF with BERT / Sentence Transformers
🌐 Deploy using Streamlit Cloud / AWS / GCP
📊 Add recruiter analytics dashboard
🤖 AI-based skill gap recommendations
📄 LinkedIn profile parsing support
🔐 Add authentication system for HR login
📡 Real-time resume ranking API
