from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

def resume_analyze(file_path: str):
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    resume_text = ""
    for doc in documents:
        resume_text += doc.page_content + "\n"

    model = ChatOpenAI()

    parser = StrOutputParser()

    prompt = PromptTemplate(
    template="""
        You are an expert resume analyzer.

        Resume Text:
        {resume_text}

        Extract the following information from the resume.
        If any value is not found, return null.

        Return ONLY valid JSON. No explanation, no extra text.

        JSON format:
        {{
        "name": null,
        "age": null,
        "education": null,
        "overseas_experience": null,
        "aus_experience": null,
        "skills": null,
        "marital_status": null,
        "english_test_score": null
        }}
        """,
            input_variables=["resume_text"]
        )

    chain = prompt | model | parser

    response = chain.invoke({'resume_text':resume_text})

    return response