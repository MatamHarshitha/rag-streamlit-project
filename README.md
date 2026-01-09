# RAG-Based Document Q&A System
Technologies Used

LangChain – RAG pipelines and embeddings

OpenAI API – LLM and embeddings

FAISS – Vector search

Streamlit – Web interface

Python 3.10+

A **GenAI-powered Retrieval-Augmented Generation (RAG) system** for semantic document question answering. Built with **LangChain**, **OpenAI**, **FAISS**, and **Streamlit**.

---

## Key Features

- Load and query documents: **PDF, DOCX, TXT, CSV**
- Perform **semantic search** over document content
- Generate **answers using LLMs** based on retrieved context
- Interactive **Streamlit interface** for easy use

---

## Getting Started

1. Clone the repository:
git clone https://github.com/yourusername/rag-streamlit-project.git
cd rag-streamlit-project

2. Create a virtual environment and install dependencies:
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt

3.Add your API
  OPENAI_API_KEY=your_api_key_here

4.Run the Streamlit app by executing:
streamlit run app.py



