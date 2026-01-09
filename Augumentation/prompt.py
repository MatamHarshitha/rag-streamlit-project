from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from Vectordatabases.vectordb import vectorstore

vectorstore= vectorstore()

from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)


prompt=PromptTemplate(
    template="""
You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context does not cover the whole topic, summarize what is present.


      {context}
      Question: {question}
""",
input_variables=['context', 'question']
)





def run_rag(vectorstore, question, k= 15):
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )

    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    output = prompt.invoke({
        "context": context,
        "question": question
    })

    answer = llm.invoke(output)

    return answer.content, docs