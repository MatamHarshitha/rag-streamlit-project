import streamlit as st
from Vectordatabases.vectordb import vectorstore
from Augumentation.prompt import run_rag

st.set_page_config(page_title="RAG QA App", layout="wide")
st.title("📄 Document RAG Question Answering")
@st.cache_resource
def load_vectorstore():
    return vectorstore()

vs = load_vectorstore()

question = st.text_input(
    "Ask a question from your documents:",
    placeholder="Enter your question:"
)

if question:
    answer, docs = run_rag(vs, question)

    st.subheader("Answer")
    st.write(answer)


