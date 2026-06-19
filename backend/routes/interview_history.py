from fastapi import APIRouter, Depends
from utils.auth_dependency import get_current_user
from database.db import SessionLocal
from models.interview_history import InterviewHistory

router = APIRouter()

@router.get("/interview-history")
def get_history(
    user=Depends(get_current_user)
):

    db = SessionLocal()

    history = (
        db.query(InterviewHistory)
        .filter(
            InterviewHistory.user_id ==
            user["user_id"]
        )
        .order_by(
            InterviewHistory.id.desc()
        )
        .all()
    )

    print("USER:", user["user_id"])
    print("HISTORY COUNT:", len(history))

    db.close()

    return [
        {
            "id": item.id,
            "role": item.role,
            "score": item.score,
            "feedback": item.feedback
        }
        for item in history
    ]

    db.close()

    return [
        {
            "id": item.id,
            "role": item.role,
            "score": item.score,
            "feedback": item.feedback
        }
        for item in history
    ]