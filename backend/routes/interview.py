from fastapi import APIRouter
from pydantic import BaseModel
from services.interview_generator import generate_questions
from database.db import SessionLocal
from models.interview_history import InterviewHistory
router = APIRouter()

class InterviewRequest(BaseModel):
    role: str

class AnswerRequest(BaseModel):
    question: str
    answer: str

@router.post("/generate-question")
def generate_question(request: InterviewRequest):

    skills = [
        "Python",
        "Machine Learning",
        "SQL"
    ]

    questions = generate_questions(skills)

    return {
        "questions": questions
    }

@router.post("/evaluate-answer")
def evaluate_answer(request: AnswerRequest):

    score = min(
        len(request.answer.split()) // 10,
        10
    )

    if score >= 8:
        feedback = """
    Score: 8/10

    Strengths:
    - Detailed explanation
    - Good technical depth

    Improvements:
    - Add real-world examples
    """
    elif score >= 5:
        feedback = """
    Score: 5/10

    Strengths:
    - Basic understanding shown

    Improvements:
    - Add more technical details
    - Include examples
    """
    else:
        feedback = """
    Score: 2/10

    Strengths:
    - Attempted answer

    Improvements:
    - Explain concepts clearly
    - Add examples
    - Add technical depth
    """
    db = SessionLocal()

    record = InterviewHistory(
        user_id=1,
        question=request.question,
        answer=request.answer,
        score=score
    )

    db.add(record)
    db.commit()
    db.close()

    return {
        "feedback": feedback
    }
@router.get("/interview-history")
def interview_history():

    db = SessionLocal()

    records = db.query(
        InterviewHistory
    ).all()

    result = []

    for item in records:
        result.append({
            "id": item.id,
            "question": item.question,
            "answer": item.answer,
            "score": item.score
        })

    db.close()

    return result