from typing import Optional
from pydantic import BaseModel, Field

class JobDescription(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None

    required_skills: list[str] = Field(default_factory=list)
    preferred_skills: list[str] = Field(default_factory=list)
    responsibilities: list[str] = Field(default_factory=list)
    qualifications: list[str] = Field(default_factory=list)