from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.dependency import get_db
from models.resume import Resume
from utils.auth_dependency import get_current_user

router = APIRouter()

@router.get("/resume-feedback")
def resume_feedback(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    latest_resume = db.query(Resume).filter(
        Resume.user_id == user["user_id"]
    ).order_by(
        Resume.id.desc()
    ).first()

    if not latest_resume:
        return {
            "message": "No resume found"
        }

    skills = latest_resume.skills.split(",")

    suggestions = []

    if "Git" not in skills:
        suggestions.append(
            "Add Git and GitHub skills"
        )

    if "Docker" not in skills:
        suggestions.append(
            "Learn Docker for deployment"
        )

    if "AWS" not in skills:
        suggestions.append(
            "Learn AWS cloud services"
        )

    if "Statistics" not in skills:
        suggestions.append(
            "Add Statistics knowledge"
        )

    return {
        "resume_strengths": skills,
        "improvement_suggestions": suggestions
    }