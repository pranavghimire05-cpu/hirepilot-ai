from langchain_core.prompts import ChatPromptTemplate
SYSTEM_PROMPT = ChatPromptTemplate.from_template(

"""

You are an expert resume assistant.

Use the retrieved resume information to answer.

Resume:

{context}

Question:

{question}

"""

)