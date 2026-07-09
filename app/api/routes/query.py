import math
from fastapi import APIRouter
from app.services.vectorstore import retrieve_resume
from app.agents.resume_agent import ask_resume
from datasets import Dataset
from app.evaluation.evaluation import metrics, evaluate_rag

router = APIRouter(
    prefix="/evaluation",
    tags=["Evaluation"]
)


def clean_nan(obj):
    if isinstance(obj, dict):
        return {k: clean_nan(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [clean_nan(v) for v in obj]
    elif isinstance(obj, float):
        return None if math.isnan(obj) else obj
    return obj

@router.post("/")
def evaluate_rag_system(
    question:str,
    resume_id:str,
    ground_truth:str
    ):

    retrieved_docs = retrieve_resume(
    resume_id=resume_id,
    query = question,
    k=3
    )

    context = [doc.page_content for doc in retrieved_docs]

    generated_answer = ask_resume(
        question=question,
        resume_id=resume_id
    ).content

    dataset = Dataset.from_dict(
    {
        "user_input" : [question],
        "response": [generated_answer],
        "retrieved_contexts": [context],
        "reference": [ground_truth]
    }
    )   
    result = evaluate_rag(dataset=dataset)

    return clean_nan(result)