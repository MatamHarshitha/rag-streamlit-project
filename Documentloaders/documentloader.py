
from langchain_community.document_loaders import (
    PyMuPDFLoader,
    Docx2txtLoader,
    TextLoader,
    CSVLoader
)
import os
os.environ["TRANSFORMERS_OFFLINE"] = "1"



def allDocs(path=r"Documentloaders\docs"):
    docs = []

    # PDF files
    pdf_files = ["MLIntro.pdf", "attention.pdf"]
    for file in pdf_files:
        loader = PyMuPDFLoader(os.path.join(path, file))
        docs.extend(loader.load())

    # DOCX files 
    docx_files = ["Social Networking Application.docx"]
    for file in docx_files:
        loader = Docx2txtLoader(os.path.join(path, file))
        docs.extend(loader.load())

    # TEXT files
    txt_files = ["liverdisease.txt", "malaria_detailed.txt"]
    for file in txt_files:
        file_path = os.path.join(path, file)
        loader = TextLoader(file_path, encoding="utf-8") 
        docs.extend(loader.load())

    # CSV file
    csv_loader = CSVLoader(os.path.join(path, "Ads.csv"))
    docs.extend(csv_loader.load())

    
    return docs



