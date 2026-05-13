import streamlit as st
from Vectordatabases.vectordb import vectorstore
from Augumentation.prompt import run_rag
import pandas as pd

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

    
    if "gender" in question.lower() and "buy" in question.lower():

        df = pd.read_csv("Documentloaders/docs/Ads.csv")

        male_rate = df[df["Gender"]=="Male"]["Purchased"].mean()
        female_rate = df[df["Gender"]=="Female"]["Purchased"].mean()

        male_percent = round(male_rate * 100, 2)
        female_percent = round(female_rate * 100, 2)

        if male_rate > female_rate:
            answer = f"Males are more likely to purchase ({male_percent}%) compared to females ({female_percent}%)."
        else:
            answer = f"Females are more likely to purchase ({female_percent}%) compared to males ({male_percent}%)."

        st.subheader("Answer")
        st.write(answer)

    else:

        answer, docs = run_rag(vs, question)

        st.subheader("Answer")
        st.write(answer)