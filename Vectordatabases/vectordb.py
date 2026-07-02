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



def create_vectorstore(chunks):
    return FAISS.from_documents(
        chunks,
        OpenAIEmbeddings()
    )
=======
>>>>>>> dd42c3673c03882262d828a1402bc5946e9bb94c
    


