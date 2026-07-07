from fastapi import APIRouter, UploadFile, File
from app.services.pdf_services import extract_text_from_pdf
from app.chains.job_desc_parser import parse_job_description

router = APIRouter(
    prefix="/job_description",
    tags=["Job-Description"]
)

@router.post("/")
async def upload_job_description(file:UploadFile=File(...)):
    pdf_data = extract_text_from_pdf(file=file)
    structured_job_desc = parse_job_description(pdf_data["text"])
    return {
        "pages": pdf_data["pages"],
        "job description": structured_job_desc.model_dump()
    }
