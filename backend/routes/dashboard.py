from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.dependency import get_db
from models.interview_history import InterviewHistory
from models.job_application import JobApplication
from utils.auth_dependency import get_current_user

router = APIRouter()


@router.get("/dashboard")
def dashboard(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    interviews = (
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

    total = len(interviews)

    highest = max(
        [i.score for i in interviews],
        default=0
    )

    average = round(
        sum(i.score for i in interviews)
        / total,
        1
    ) if total else 0

    latest = (
        interviews[0].score
        if interviews
        else 0
    )

    recent = []

    for item in interviews[:5]:
        recent.append({
            "role": item.role,
            "score": item.score,
            "feedback": item.feedback
        })

    jobs = (
        db.query(JobApplication)
        .filter(
            JobApplication.user_id ==
            user["user_id"]
        )
        .all()
    )

    total_applications = len(jobs)

    applied_count = len(
        [j for j in jobs if j.status == "Applied"]
    )

    interview_count = len(
        [j for j in jobs if j.status == "Interview"]
    )

    selected_count = len(
        [j for j in jobs if j.status == "Selected"]
    )

    rejected_count = len(
        [j for j in jobs if j.status == "Rejected"]
    )

    return {
        "total_interviews": total,
        "highest_score": highest,
        "average_score": average,
        "latest_score": latest,

        "recent_interviews": recent,

        "total_applications": total_applications,
        "applied_count": applied_count,
        "interview_count": interview_count,
        "selected_count": selected_count,
        "rejected_count": rejected_count
    }