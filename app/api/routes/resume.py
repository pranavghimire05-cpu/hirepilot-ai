from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services.pdf_services import extract_text_from_pdf
from app.chains.resume_parser import parse_resume

router  = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

@router.get("/")
def health():
    return {"message" : "healthy"}

@router.post("/parse-resume")

async def parse_resume_endpoint(

    file: UploadFile = File(...)

):

    pdf_data = extract_text_from_pdf(file)

    structured_resume = parse_resume(pdf_data["text"])

    return {

        "pages": pdf_data["pages"],

        "resume": structured_resume.model_dump()

    }