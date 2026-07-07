from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services.pdf_services import extract_text_from_pdf

router  = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

@router.get("/")
def health():
    return {"message" : "healthy"}

@router.post("/upload")
async def upload_resume(file : UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=404,
            detail="Invalid file type"
        )
    result = extract_text_from_pdf(file=file)
    return {
        "file_name": file.filename,
        **result
    }