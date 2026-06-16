from fastapi import APIRouter
from pydantic import BaseModel

from database.db import SessionLocal
from models.job_application import JobApplication

router = APIRouter()

class JobRequest(BaseModel):
    company: str
    role: str
    status: str


@router.post("/add-job")
def add_job(request: JobRequest):

    db = SessionLocal()

    job = JobApplication(
        user_id=1,
        company=request.company,
        role=request.role,
        status=request.status
    )

    db.add(job)
    db.commit()

    db.close()

    return {"message": "Job Added"}

@router.get("/jobs-history")
def jobs_history():

    db = SessionLocal()

    jobs = db.query(
        JobApplication
    ).all()

    result = []

    for job in jobs:
        result.append({
            "id": job.id,
            "company": job.company,
            "role": job.role,
            "status": job.status
        })

    db.close()

    return result