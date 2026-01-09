from langchain_community.document_loaders import PyMuPDFLoader


doc =PyMuPDFLoader(r"D:\DocumentAgent\Documentloaders\docs\attention.pdf")
docs = doc.load()
print(docs[0].page_content)