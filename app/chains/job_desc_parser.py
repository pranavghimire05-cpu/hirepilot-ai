from langchain_core.prompts import ChatPromptTemplate
from app.prompts.job_description_parser import SYSTEM_PROMPT
from app.schemas.job_description import JobDescription
from app.llm.llm_model import get_llm

llm = get_llm()

prompts = ChatPromptTemplate.from_messages(
    [
        ("system",SYSTEM_PROMPT),
        ("human",
         """
            Extract the structured information from following job description text.

            Text:
            {text}
        """
         )
    ]
)



structured_llm = llm.with_structured_output(JobDescription)


job_description_chain = prompts | structured_llm

def parse_job_description(text:str):
    return job_description_chain.invoke(
        {
            "text": text
        }
    )