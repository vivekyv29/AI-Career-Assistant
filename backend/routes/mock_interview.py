from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class MockInterviewRequest(BaseModel):
    role: str

class SubmitInterviewRequest(BaseModel):
    answers: list[str]

@router.post("/start-mock-interview")
def start_mock_interview(request: MockInterviewRequest):

    questions = [
        "What is Python?",
        "What is OOP?",
        "What is Machine Learning?",
        "What is SQL JOIN?",
        "Explain Random Forest."
    ]

    return {
        "questions": questions
    }

@router.post("/submit-mock-interview")
def submit_mock_interview(request: SubmitInterviewRequest):

    total_score = 0

    for answer in request.answers:
        score = min(len(answer.split()) // 10, 10)
        total_score += score

    final_score = round(
        total_score / len(request.answers)
    )

    return {
        "score": final_score
    }