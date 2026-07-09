from app.llm.llm_model import get_llm
from app.services.vectorstore import retrieve_resume
from app.prompts.resume_agent import SYSTEM_PROMPT

llm = get_llm()

def ask_resume(question:str, resume_id:str):
    context = retrieve_resume(query=question, resume_id=resume_id)
    chain = SYSTEM_PROMPT | llm
    return chain.invoke({
        "context":context,
        "question":question
    })


