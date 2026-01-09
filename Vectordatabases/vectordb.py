from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from TextSplitter.TextSplitter import splitdocs
from Documentloaders.documentloader import allDocs
from dotenv import load_dotenv

load_dotenv()

docs = allDocs()
chunks = splitdocs(docs)



vectorstore = FAISS.from_documents(
    chunks,
       OpenAIEmbeddings()
)

def vectorstore():
    docs = allDocs()
    chunks = splitdocs(docs)
    vectorstore = FAISS.from_documents(
       chunks,
       OpenAIEmbeddings()
)
    
    return vectorstore
    


