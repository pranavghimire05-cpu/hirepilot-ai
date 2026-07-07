from pydantic import BaseModel, Field


class Resume(BaseModel):
    name: str = Field(description="Candidate full name")
    email: str = Field(description="Candidate email")
    skills: list[str] = Field(default_factory=list)
    education: list[str] = Field(default_factory=list)
    experience: list[str] = Field(default_factory=list)
    projects: list[str] = Field(default_factory=list)