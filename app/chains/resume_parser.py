from langchain_core.prompts import ChatPromptTemplate
from app.llm.llm_model import get_llm
from app.schemas.resume import Resume
from app.prompts.resume_parser import SYSTEM_PROMPT

llm = get_llm()

structured_llm = llm.with_structured_output(Resume)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("human",

            """

            Extract the structured information from the following resume.

            Resume:

            {resume}

            """)

    ]
)
resume_chain = prompt | structured_llm

def parse_resume(text: str):
    return resume_chain.invoke(
        {
            "resume": text
        }
    )

def resume_to_text(resume: Resume) -> str:
    return f"""
    Name:
    {resume.name}

    Email:
    {resume.email}

    Skills:
    {chr(10).join(resume.skills)}

    Education:
    {chr(10).join(resume.education)}

    Experience:
    {chr(10).join(resume.experience)}

    Projects:
    {chr(10).join(resume.projects)}
    """