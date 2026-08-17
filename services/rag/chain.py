import os
from langchain_openai import ChatOpenAI  # <-- [UPDATED]
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from app.services.rag.retriever import get_retriever

PROMPT_TEMPLATE = """
You are an expert AI Visa Consultant assistant. Use the following official visa guidelines and context to answer the user's question accurately.

Context from official guidelines:
{context}

Question: {question}

Instructions:
1. Answer strictly based on the provided context.
2. If the answer is not contained in the context, state clearly: "I couldn't find specific official guidelines regarding this in the system database."
3. Keep the tone professional, structured, and helpful.

Answer:
"""

def generate_rag_response(question: str):
    retriever = get_retriever(k=4)
    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])
    
    sources = [
        {
            "source": doc.metadata.get("source", "Unknown"),
            "page": doc.metadata.get("page", 1)
        } for doc in docs
    ]

    # OpenAI GPT-4o-mini model
    llm = ChatOpenAI(
        model="gpt-4o-mini",  
        temperature=0.2,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

    chain = (
        {"context": lambda x: context, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    answer = chain.invoke(question)

    return {
        "question": question,
        "answer": answer,
        "sources": sources
    }