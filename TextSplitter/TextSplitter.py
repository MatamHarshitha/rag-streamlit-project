import sys
import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from Documentloaders.documentloader import allDocs




splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", " ", ""]
)

def splitdocs(docs):
    chunks =splitter.split_documents(docs)
    return chunks


