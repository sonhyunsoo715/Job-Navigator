from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    company = Column(String(255))
    location = Column(String(100))
    experience = Column(String(50))
    tech_stack = Column(String(255))
    description = Column(Text)
    url = Column(String(255))
    job_type = Column(String(50))