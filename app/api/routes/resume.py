from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services.pdf_services import extract_text_from_pdf
from app.chains.resume_parser import parse_resume, resume_to_text
from app.services.chunk import chunk_generator
from app.services.vectorstore import store_resume

router  = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

@router.get("/")
def health():
    return {"message" : "healthy"}

@router.post("/upload-resume")

async def upload_resume(file: UploadFile = File(...)):

    try:

        # Parse resume
        pdf_byte = extract_text_from_pdf(file=file)

        resume = parse_resume(text=pdf_byte)

        resume_text = resume_to_text(resume)



        # Create chunks

        chunks = chunk_generator(resume_text)

        # Store in Chroma

        resume_id = store_resume(chunks)

        return {

            "message": "Resume uploaded successfully",

            "resume_id": resume_id,

            "chunks_stored": len(chunks)

        }

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )