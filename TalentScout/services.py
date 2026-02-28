from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import re
import json
import os
from dotenv import load_dotenv
load_dotenv()

def get_llm():    
    groq_api_key = os.getenv("GROQ_API_KEY")
    llm = ChatGroq(groq_api_key=groq_api_key,model_name="openai/gpt-oss-120b", temperature=0.7)
    return llm

def create_prompt():
    from prompts import question_generation_prompt
    prompt = ChatPromptTemplate.from_messages([("system", question_generation_prompt),("human", "{skills}")])
    return prompt

def is_valid_phone(phone: str) -> bool:
    return re.match(r'^[6-9]\d{9}$', phone) is not None

def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def generate_questions(skills: str):

    llm = get_llm()
    prompt = create_prompt()

    chain = prompt | llm

    try:
        response = chain.invoke({"skills": skills})

        # LLM response content
        raw_output = response.content.strip()

        # Convert string JSON to Python dict
        parsed_output = json.loads(raw_output)

        return parsed_output

    except Exception as e:
        print("LLM Parsing Error:", e)

        return {
            "is_questions": False,
            "skills": [],
            "questions": []
        }