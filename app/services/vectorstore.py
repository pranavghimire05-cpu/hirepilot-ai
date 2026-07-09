import os
from langchain_chroma import Chroma
import uuid
from langchain_mistralai.embeddings import MistralAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MISTRAL_API_KEY")

embedding_function = MistralAIEmbeddings(
    model="mistral-embed",
    api_key=API_KEY
)

vector_store = Chroma(
        collection_name="resume",
        embedding_function=embedding_function,
        persist_directory="./chroma_db"
    )

def store_resume(chunks: list[str]) -> str:


    resume_id = str(uuid.uuid4())

    metadatas = [

        {

            "resume_id": resume_id,

            "chunk_id": idx,

            "source": "resume",

        }

        for idx in range(len(chunks))

    ]

    vector_store.add_texts(

        texts=chunks,

        metadatas=metadatas,

    )

    return resume_id

def retrieve_resume(resume_id: str, query: str, k: int = 5):

    """

    Retrieve the most relevant chunks for a specific resume.

    """

    return vector_store.similarity_search(

        query=query,

        k=k,

        filter={"resume_id": resume_id},

    )

def delete_resume(resume_id: str):

    """

    Delete every chunk belonging to a resume.

    """

    docs = vector_store.get(

        where={"resume_id": resume_id}

    )

    ids = docs["ids"]

    if ids:

        vector_store.delete(ids=ids)