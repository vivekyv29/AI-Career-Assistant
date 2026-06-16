from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database.dependency import get_db

from models.resume import Resume

from services.recommender import recommend_jobs

from utils.auth_dependency import get_current_user

router = APIRouter()

@router.get("/job-recommendations")
def get_recommendations(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    resume = db.query(Resume).filter(
        Resume.user_id == user["user_id"]
    ).first()

    if not resume:
        return {
            "jobs": []
        }

    skills = resume.skills.split(",")

    jobs = recommend_jobs(skills)

    return {
        "jobs": jobs
    }