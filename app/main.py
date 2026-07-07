from fastapi import FastAPI
from app.api.routes.resume import router as resume_router
from app.api.routes.job_description import router as job_router

app = FastAPI(
    title="hirepilot-ai",
    version="1.0.0"
)

app.include_router(resume_router)
app.include_router(job_router)

@app.get("/")
def root():
    return {"message": "Welcome to HirePilot AI"}


