import streamlit as st
from ingestion import extract_from_pdf, extract_from_excel
from qa_engine import build_qa_engine, answer_question
from utils import format_tables

st.set_page_config(page_title="Financial Document Q&A", layout="wide")
st.title("📊 Financial Document Q&A Assistant")

uploaded_file = st.file_uploader("Upload PDF or Excel", type=["pdf", "xlsx"])

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        text, tables = extract_from_pdf(uploaded_file)
        dfs = format_tables(tables)
    else:
        dfs = extract_from_excel(uploaded_file)
        text = "\n".join([df.to_string() for df in dfs.values()])

    st.success("✅ Document processed successfully")
    st.subheader("📄 Extracted Data Preview")
    for df in (dfs if isinstance(dfs, list) else dfs.values()):
        st.dataframe(df)

    chain = build_qa_engine()

    st.subheader("💬 Ask Questions")
    question = st.text_input("Type your question (e.g., 'What is total revenue?')")
    if question:
        answer = answer_question(chain, text, question)
        st.write("**AI Response:**", answer)
