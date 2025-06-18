from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.job import Job  # 너의 Job 모델
from collections import defaultdict
import json

router = APIRouter(prefix="/api/trend", tags=["trend"])

@router.get("/skills")
def get_jobtype_tech_stack_trend(db: Session = Depends(get_db)):
    result = db.query(Job.job_type, Job.tech_stack).all()

    # 기술 스택을 쉼표로 분해해서 카운트
    freq = defaultdict(lambda: defaultdict(int))
    for job_type, tech_stack in result:
        if tech_stack:
            for tech in tech_stack.split(","):
                freq[job_type][tech.strip()] += 1

    # 직무별 데이터를 리스트로 변환
    response = []
    for job_type, skills in freq.items():
        for tech, count in skills.items():
            response.append({
                "job_type": job_type,
                "tech_stack": tech,
                "frequency": count
            })

    return {"items": response}
