from fastapi import FastAPI
from app.api.routes.resume import router as resume_router

app = FastAPI(
    title="hirepilot-ai",
    version="1.0.0"
)

app.include_router(resume_router)

@app.get("/")
def root():
    return {"message": "Welcome to HirePilot AI"}


