
from langchain_community.document_loaders import (
    PyMuPDFLoader,
    Docx2txtLoader,
    TextLoader,
    CSVLoader
)

import os

os.environ["TRANSFORMERS_OFFLINE"] = "1"

# Get absolute path of current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to docs folder
DOCS_PATH = os.path.join(BASE_DIR, "docs")


def allDocs():

    docs = []

    # PDF files
    pdf_files = ["MLIntro.pdf", "attention.pdf"]

    for file in pdf_files:

        file_path = os.path.join(DOCS_PATH, file)

        print(file_path)

        loader = PyMuPDFLoader(file_path)

        docs.extend(loader.load())

    # DOCX files
    docx_files = ["Social Networking Application.docx"]

    for file in docx_files:

        file_path = os.path.join(DOCS_PATH, file)

        loader = Docx2txtLoader(file_path)

        docs.extend(loader.load())

    # TEXT files
    txt_files = ["liverdisease.txt", "malaria_detailed.txt"]

    for file in txt_files:

        file_path = os.path.join(DOCS_PATH, file)

        loader = TextLoader(file_path, encoding="utf-8")

        docs.extend(loader.load())

    # CSV files
    csv_path = os.path.join(DOCS_PATH, "Ads.csv")

    csv_loader = CSVLoader(csv_path)

    docs.extend(csv_loader.load())

    return docs