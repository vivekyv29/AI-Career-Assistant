from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import Depends
from utils.auth_dependency import get_current_user
from services.chatbot_service import ask_ollama
from database.db import SessionLocal
from models.resume import Resume
from models.interview_history import InterviewHistory

import json
import re

router = APIRouter()


class MockInterviewRequest(BaseModel):
    role: str


class SubmitInterviewRequest(BaseModel):
    role: str
    answers: list[str]


@router.post("/start-mock-interview")
def start_mock_interview(
    request: MockInterviewRequest,
    user=Depends(get_current_user)
):

    db = SessionLocal()

    resume = db.query(
        Resume
    ).filter(
        Resume.user_id == user["user_id"]
    ).first()

    resume_text = ""

    if resume:
        resume_text = getattr(
            resume,
            "resume_text",
            ""
        )

    db.close()

    try:

        prompt = f"""
Generate 10 interview questions.

ROLE:
{request.role}

RESUME:
{resume_text}

Generate questions based on:
- Resume Projects
- Technical Skills
- Experience
- Target Role

Mix:
- Technical Questions
- HR Questions
- Scenario Based Questions

One question per line.
"""

        result = ask_ollama(prompt)

        questions = []

        for q in result.split("\n"):

            q = q.strip()

            if (
                q
                and len(q) > 10
                and "question" not in q.lower()
            ):
                questions.append(q)

        if len(questions) < 5:
            raise Exception()

        return {
            "questions": questions[:10]
        }

    except Exception:

        return {
            "questions": [
                "Tell me about yourself.",
                "Explain your strongest project.",
                "What are your strengths?",
                "What are your weaknesses?",
                "How do you solve problems?",
                "Describe a challenge you faced.",
                "Explain a technology you recently learned.",
                "How do you handle deadlines?",
                "Why should we hire you?",
                "Where do you see yourself in 5 years?"
            ]
        }
@router.post("/submit-mock-interview")
def submit_mock_interview(
    request: SubmitInterviewRequest,
    user=Depends(get_current_user)
):

    answered = len(
        [a for a in request.answers if a.strip()]
    )

    if answered == 0:

        return {
            "overall_score": 0,
            "technical_score": 0,
            "communication_score": 0,
            "problem_solving_score": 0,
            "confidence_score": 0,
            "strengths": [],
            "weaknesses": [
                "No answers submitted"
            ],
            "recommendation":
                "Complete the interview first"
        }

    all_answers = "\n".join(
        request.answers
    )

    prompt = f"""
You are an expert technical interviewer.

Role:
{request.role}

Candidate Answers:
{all_answers}

Evaluate the candidate honestly.

Return ONLY valid JSON:

{{
  "technical_score": 35,
  "communication_score": 16,
  "problem_solving_score": 17,
  "confidence_score": 15,
  "strengths": [
    "Strong Python knowledge",
    "Good problem solving",
    "Clear explanations"
  ],
  "weaknesses": [
    "Needs better SQL",
    "Limited project depth",
    "Can improve communication"
  ],
  "recommendation":
    "Focus on SQL, system design and interview practice."
}}
"""

    try:

        result = ask_ollama(prompt)

        match = re.search(
            r"\{.*\}",
            result,
            re.DOTALL
        )

        if not match:
            raise Exception(
                "Invalid JSON from Ollama"
            )

        report = json.loads(
            match.group()
        )

        overall = (
            report["technical_score"]
            + report["communication_score"]
            + report["problem_solving_score"]
            + report["confidence_score"]
        )

        db = SessionLocal()

        history = InterviewHistory(
            user_id=user["user_id"],
            role=request.role,
            question="Mock Interview",
            answer=all_answers,
            score=overall,
            feedback=report["recommendation"]
        )

        db.add(history)
        db.commit()
        db.close()

        return {
            "overall_score": overall,
            **report
        }

    except Exception as e:

        print("INTERVIEW ERROR =", e)

        score = min(
            100,
            answered * 10
        )

        db = SessionLocal()

        history = InterviewHistory(
            user_id=user["user_id"],
            role=request.role,
            question="Mock Interview",
            answer=all_answers,
            score=score,
            feedback="Ollama evaluation failed"
        )

        db.add(history)
        db.commit()
        db.close()

        return {
            "overall_score": score,
            "technical_score": int(score * 0.4),
            "communication_score": int(score * 0.2),
            "problem_solving_score": int(score * 0.2),
            "confidence_score": int(score * 0.2),
            "strengths": [
                "Attempted interview"
            ],
            "weaknesses": [
                "Ollama evaluation failed"
            ],
            "recommendation":
                "Practice more and retry"
        }