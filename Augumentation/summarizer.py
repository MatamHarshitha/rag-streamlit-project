from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2
)

summary_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
You are an expert document summarizer.

Summarize the following document.

Include:
- Main topic
- Key points
- Important facts
- Final conclusion

Document:

{text}
"""
)


def summarize_document(text):

    chain = summary_prompt | llm

    response = chain.invoke({"text": text})

    return response.content