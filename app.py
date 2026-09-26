import streamlit as st
import json
import os
from main import GeminiATSEvaluator  # Main script se Class import kar rahe hain

st.set_page_config(page_title="AIVI ATS Resume Matcher", page_icon="🤖", layout="wide")

st.title("🤖 AIVI Intelligence - ATS Evaluation Engine")
st.markdown("AI-powered resume matching with strict JSON schema validation.")

# Sidebar for API Key
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

# Input columns
col1, col2 = st.columns(2)

with col1:
    jd_text = st.text_area("📌 Job Description (JD)", height=250, placeholder="Paste JD here...")

with col2:
    resume_text = st.text_area("📄 Resume Content", height=250, placeholder="Paste Resume text here...")

# Run Button
if st.button("🚀 Run ATS Evaluation", use_container_width=True):
    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar.")
    elif not jd_text or not resume_text:
        st.warning("Please provide both JD and Resume text.")
    else:
        with st.spinner("Analyzing resume against JD using Gemini API..."):
            evaluator = GeminiATSEvaluator(api_key=api_key)
            result = evaluator.evaluate_resume(resume_text=resume_text, jd_text=jd_text)
            
            st.subheader("📊 Evaluation Output (JSON)")
            st.json(result)
