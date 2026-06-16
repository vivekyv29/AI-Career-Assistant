from fastapi import APIRouter
from database.db import SessionLocal
from models.resume import Resume
from models.interview_history import InterviewHistory

router = APIRouter()

@router.get("/dashboard")
def dashboard():

    db = SessionLocal()

    total_resumes = db.query(Resume).count()

    total_interviews = db.query(
        InterviewHistory
    ).count()

    avg_score = 0

    scores = db.query(
        InterviewHistory
    ).all()

    if scores:
        avg_score = sum(
            item.score for item in scores
        ) / len(scores)

    db.close()

    return {
        "total_resumes": total_resumes,
        "total_interviews": total_interviews,
        "average_score": round(avg_score, 2)
    }