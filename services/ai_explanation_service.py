import requests 
import os 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()


def generate_ai_explanation(age,education,aus_experience,language,score,visa):
    llm = ChatOpenAI()
    prompt = PromptTemplate(
        template="""
        You are an Australian visa consultant.
        User details:
        Age : {age}
        Education : {education}
        Australian_experience : {aus_experience}
        Language : {language}
        Score : {score}
        Recommended visa :{visa}
        Please provide:
        1. Why this visa is recommended for this user
        2. What are the user's strengths
        3. What can be improved to get better visa options
        4. Next steps to take
        
        Keep the response detailed but easy to understand.
    """,
    input_variables=['age','education','aus_experience','language','score','visa']
    )

    chain = prompt | llm | StrOutputParser()

    result = chain.invoke({'age':age,'education':education,'aus_experience':aus_experience,'language':language,'score':score,'visa':visa})

    return result
