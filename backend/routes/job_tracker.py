from fastapi import APIRouter, Depends
from pydantic import BaseModel

from database.db import SessionLocal
from models.job_application import JobApplication
from utils.auth_dependency import get_current_user

router = APIRouter()

class JobRequest(BaseModel):
    company: str
    role: str
    status: str


@router.post("/add-job")
def add_job(
    request: JobRequest,
    user=Depends(get_current_user)
):
    print("LOGGED USER =", user)
    print("SAVING JOB FOR =", user["user_id"])
    db = SessionLocal()

    job = JobApplication(
        user_id=user["user_id"],
        company=request.company,
        role=request.role,
        status=request.status
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    db.close()

    return {
        "message": "Job Added Successfully"
    }
@router.get("/jobs-history")
def jobs_history(
    user=Depends(get_current_user)
):

    db = SessionLocal()

    jobs = (
        db.query(JobApplication)
        .filter(
            JobApplication.user_id ==
            user["user_id"]
        )
        .all()
    )

    result = []

    for job in jobs:
        result.append({
            "id": job.id,
            "company": job.company,
            "role": job.role,
            "status": job.status,
            "created_at": job.created_at
        })

    db.close()

    return result