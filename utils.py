import pdfplumber
import docx
import re
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer


# -----------------------------
# Resume Text Extraction
# -----------------------------
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text


def extract_resume_text(uploaded_file):
    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)

    elif file_name.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)

    else:
        return ""


# -----------------------------
# Text Cleaning / Preprocessing
# -----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"\n+", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text.strip()


# -----------------------------
# TF-IDF Matching
# -----------------------------
def tfidf_resume_matching(resume_texts, job_description):
    corpus = [job_description] + resume_texts

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(corpus)

    jd_vector = tfidf_matrix[0]
    resume_vectors = tfidf_matrix[1:]

    similarity_scores = cosine_similarity(jd_vector, resume_vectors).flatten()
    return similarity_scores


# -----------------------------
# Embedding Matching
# -----------------------------
def embedding_resume_matching(resume_texts, job_description):
    model = SentenceTransformer("all-MiniLM-L6-v2")

    jd_embedding = model.encode(job_description)
    resume_embeddings = model.encode(resume_texts)

    similarity_scores = cosine_similarity([jd_embedding], resume_embeddings).flatten()
    return similarity_scores


# -----------------------------
# Skill Extraction (Basic)
# -----------------------------
SKILLS_LIST = [
    "python", "java", "sql", "machine learning", "deep learning", "nlp",
    "tensorflow", "pytorch", "data analysis", "pandas", "numpy",
    "matplotlib", "seaborn", "power bi", "tableau", "excel",
    "aws", "gcp", "azure", "docker", "kubernetes", "spark",
    "hadoop", "scikit learn", "flask", "streamlit", "fastapi",
    "git", "github", "linux"
]


def extract_skills(text):
    found_skills = []
    for skill in SKILLS_LIST:
        if skill in text.lower():
            found_skills.append(skill)
    return list(set(found_skills))


# -----------------------------
# Missing Skills Finder
# -----------------------------
def missing_skills(job_description, resume_text):
    jd_skills = extract_skills(job_description)
    resume_skills = extract_skills(resume_text)

    missing = list(set(jd_skills) - set(resume_skills))
    return jd_skills, resume_skills, missing


# -----------------------------
# Create Final Ranking DataFrame
# -----------------------------
def create_ranking_dataframe(resume_names, scores):
    df = pd.DataFrame({
        "Resume": resume_names,
        "Similarity Score": scores
    })

    df["Similarity Score"] = df["Similarity Score"].round(4)
    df = df.sort_values(by="Similarity Score", ascending=False).reset_index(drop=True)
    df.index = df.index + 1
    df.rename_axis("Rank", inplace=True)

    return df