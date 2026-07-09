
from ragas import evaluate

from app.llm.llm_model import get_llm
from app.services.vectorstore import embedding_function
from app.services.vectorstore import retrieve_resume
from ragas.metrics import (

    Faithfulness,

    AnswerRelevancy,

    ContextPrecision,

    ContextRecall,

)

llm = get_llm()

metrics = [
            Faithfulness(),
            AnswerRelevancy(),
            ContextRecall(),
            ContextPrecision()
        ]

def evaluate_rag(dataset):
    result =  evaluate(
        dataset=dataset,
        metrics = metrics,
        embeddings=embedding_function,
        llm=llm
    )
    return result.to_pandas().to_dict(orient="records")[0]