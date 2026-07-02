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
<<<<<<< HEAD
=======

>>>>>>> f87d671a3494ea0213b4c426a6390e401126535d



def create_vectorstore(chunks):
    return FAISS.from_documents(
        chunks,
        OpenAIEmbeddings()
    )
<<<<<<< HEAD
=======

>>>>>>> f87d671a3494ea0213b4c426a6390e401126535d
    


