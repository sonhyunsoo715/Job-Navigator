from pydantic import BaseModel
from typing import Optional

class JobBase(BaseModel):
    title: str
    company: Optional[str] = None
    location: Optional[str] = None
    experience: Optional[str] = None
    tech_stack: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    job_type: Optional[str] = None

class JobCreate(JobBase):
    pass

class JobUpdate(BaseModel):  # 업데이트는 전부 optional
    title: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    experience: Optional[str] = None
    tech_stack: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    job_type: Optional[str] = None

class JobOut(JobBase):
    id: int

    class Config:
         from_attributes = True
