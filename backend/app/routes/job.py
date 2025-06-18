from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.job import Job
from schemas.job_schema import JobCreate, JobUpdate, JobOut

router = APIRouter(prefix="/jobs", tags=["jobs"])

@router.get("/", response_model=list[JobOut])
def read_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()

@router.post("/", response_model=JobOut)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    db_job = Job(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.put("/{job_id}", response_model=JobOut)
def update_job(job_id: int, job: JobUpdate, db: Session = Depends(get_db)):
    db_job = db.query(Job).get(job_id)
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    for key, value in job.dict(exclude_none=True).items():
        setattr(db_job, key, value)
    db.commit()
    db.refresh(db_job)
    return db_job
