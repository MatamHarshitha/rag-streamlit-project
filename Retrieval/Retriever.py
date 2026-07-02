from Vectordatabases.vectordb import vectorstore

vectorstore= vectorstore()
query=[
       "What are Severe malaria symptoms",
       "What are Compound structures",
       "What is Multi-head Attention"
       ]

retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k":2})
retrieved_docs=[]

for question in query:
    docs=retriever.invoke(question)
    print(f"\nQuery: {question}")
    for doc in docs:
        print("-", doc.page_content)
   



