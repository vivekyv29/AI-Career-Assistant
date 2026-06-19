from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import Depends
from database.db import SessionLocal

from models.resume import Resume
from models.interview_history import InterviewHistory

from utils.auth_dependency import get_current_user
from services.chatbot_service import ask_ollama

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(
    request: ChatRequest,
    user=Depends(get_current_user)
):

    db = SessionLocal()

    resume = (
        db.query(Resume)
        .filter(
            Resume.user_id ==
            user["user_id"]
        )
        .first()
    )

    interviews = (
        db.query(InterviewHistory)
        .filter(
            InterviewHistory.user_id ==
            user["user_id"]
        )
        .all()
    )

    skills = []

    if resume and resume.skills:
        skills = resume.skills.split(",")

    resume_text = ""

    if resume and resume.resume_text:
        resume_text = (
            resume.resume_text[:3000]
        )

    avg_score = 0

    if interviews:
        avg_score = round(
            sum(i.score for i in interviews)
            / len(interviews),
            1
        )

    prompt = f"""
You are an AI Career Assistant.

Candidate Skills:
{', '.join(skills)}

Average Interview Score:
{avg_score}

Resume:
{resume_text}

Question:
{request.message}

Rules:
- Give career guidance
- Suggest skills to learn
- Recommend projects
- Recommend interview preparation
- Be specific to the candidate profile
"""

    result = ask_ollama(prompt)

    db.close()

    return {
        "response": result
    }