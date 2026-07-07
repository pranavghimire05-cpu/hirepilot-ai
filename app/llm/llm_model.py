import os
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

def get_llm():
    llm=ChatMistralAI(
        model_name="mistral-medium-latest",
        temperature=0,
        api_key=MISTRAL_API_KEY
    )
    return llm