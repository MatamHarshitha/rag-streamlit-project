import streamlit as st
import os

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

from Augumentation.prompt import run_rag
from Augumentation.summarizer import summarize_document
from Documentloaders.documentloader import load_uploaded_document
from TextSplitter.TextSplitter import splitdocs
from Vectordatabases.vectordb import vectorstore

st.set_page_config(page_title="RAG QA App", layout="wide")

st.title("📄 Document RAG Question Answering")


@st.cache_resource
def load_vectorstore():
    return vectorstore()


source = st.radio(
    "Choose Source",
    ["Existing Documents", "Upload Document"]
)


if source == "Existing Documents":

    question = st.text_input("Ask a question")

    if st.button("Ask"):

        if question.strip():

            vs = load_vectorstore()

            answer, docs = run_rag(vs, question)

            st.subheader("Answer")
            st.write(answer)

        else:

            st.warning("Please enter a question.")


else:

    uploaded_file = st.file_uploader(
        "Upload a document",
        type=["pdf", "docx", "txt", "csv"],
        key="uploaded_document"
    )

    if uploaded_file:

        os.makedirs("uploads", exist_ok=True)

        file_path = os.path.join("uploads", uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        if (
            "uploaded_vs" not in st.session_state
            or st.session_state.get("filename") != uploaded_file.name
        ):

            text = load_uploaded_document(file_path)

            document = Document(page_content=text)

            chunks = splitdocs([document])

            st.session_state.uploaded_vs = FAISS.from_documents(
                chunks,
                OpenAIEmbeddings()
            )

            st.session_state.filename = uploaded_file.name

        mode = st.radio(
            "Choose Action",
            ["Summarize", "Ask Questions"]
        )

        if mode == "Summarize":

            if st.button("Generate Summary"):

                text = load_uploaded_document(file_path)

                summary = summarize_document(text)

                st.subheader("Summary")
                st.write(summary)

        else:

            question = st.text_input("Ask a question about the uploaded document")

            if st.button("Ask Uploaded Document"):

                if question.strip():

                    answer, docs = run_rag(
                        st.session_state.uploaded_vs,
                        question
                    )

                    st.subheader("Answer")
                    st.write(answer)

                else:

                    st.warning("Please enter a question.")
