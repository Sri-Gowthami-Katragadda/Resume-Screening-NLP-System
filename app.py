import streamlit as st
import pandas as pd
from utils import (
    extract_resume_text,
    clean_text,
    tfidf_resume_matching,
    embedding_resume_matching,
    create_ranking_dataframe,
    missing_skills
)

st.set_page_config(page_title="Resume Screening System", layout="wide")

st.title("📄 Resume Screening System (NLP Project)")
st.write("Upload resumes + paste Job Description → get best matching resumes ranked automatically.")

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("⚙️ Settings")

matching_method = st.sidebar.selectbox(
    "Choose Matching Method",
    ["TF-IDF (Fast & Simple)", "Embeddings (Semantic Matching)"]
)

threshold = st.sidebar.slider("Minimum Similarity Threshold", 0.0, 1.0, 0.3)

# -----------------------------
# Upload resumes
# -----------------------------
uploaded_resumes = st.file_uploader(
    "📌 Upload Resumes (PDF/DOCX)",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

job_description = st.text_area("📝 Paste Job Description Here", height=200)

# -----------------------------
# Run Screening
# -----------------------------
if st.button("🔍 Screen Resumes"):

    if not uploaded_resumes:
        st.error("Please upload at least 1 resume.")
        st.stop()

    if job_description.strip() == "":
        st.error("Please paste Job Description.")
        st.stop()

    resume_texts = []
    resume_names = []

    st.info("Extracting and cleaning resume texts...")

    for file in uploaded_resumes:
        text = extract_resume_text(file)
        cleaned = clean_text(text)

        resume_texts.append(cleaned)
        resume_names.append(file.name)

    cleaned_jd = clean_text(job_description)

    # -----------------------------
    # Similarity Calculation
    # -----------------------------
    if matching_method == "TF-IDF (Fast & Simple)":
        scores = tfidf_resume_matching(resume_texts, cleaned_jd)
    else:
        scores = embedding_resume_matching(resume_texts, cleaned_jd)

    # -----------------------------
    # Ranking DataFrame
    # -----------------------------
    df_ranked = create_ranking_dataframe(resume_names, scores)

    st.subheader("📊 Ranked Resume Matches")
    st.dataframe(df_ranked, use_container_width=True)

    # -----------------------------
    # Threshold Filtering
    # -----------------------------
    filtered_df = df_ranked[df_ranked["Similarity Score"] >= threshold]

    st.subheader(f"✅ Resumes Above Threshold ({threshold})")
    if filtered_df.empty:
        st.warning("No resumes matched above threshold.")
    else:
        st.dataframe(filtered_df, use_container_width=True)

    # -----------------------------
    # Download CSV
    # -----------------------------
    csv = df_ranked.to_csv(index=True).encode("utf-8")

    st.download_button(
        label="📥 Download Ranking CSV",
        data=csv,
        file_name="resume_ranking_results.csv",
        mime="text/csv"
    )

    # -----------------------------
    # Skill Gap Analysis
    # -----------------------------
    st.subheader("🛠 Skill Gap Analysis (Top Resume)")

    top_resume_name = df_ranked.iloc[0]["Resume"]
    top_resume_index = resume_names.index(top_resume_name)
    top_resume_text = resume_texts[top_resume_index]

    jd_skills, resume_skills, missing = missing_skills(cleaned_jd, top_resume_text)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("### 📌 JD Skills")
        st.write(jd_skills)

    with col2:
        st.write("### 📄 Resume Skills")
        st.write(resume_skills)

    with col3:
        st.write("### ❌ Missing Skills")
        st.write(missing)

    st.success("Resume Screening Completed Successfully ✅")