from fastapi import APIRouter
from pydantic import BaseModel

from services.chatbot_service import ask_gemini

router = APIRouter()

class CoverLetterRequest(BaseModel):
    name: str
    job_role: str
    skills: list[str]

@router.post("/cover-letter")
def generate_cover_letter(
    request: CoverLetterRequest
):

    prompt = f"""
    Write a professional cover letter.

    Name: {request.name}

    Job Role: {request.job_role}

    Skills:
    {", ".join(request.skills)}

    Make it professional and ATS friendly.
    """

    cover_letter = ask_gemini(prompt)

    return {
        "cover_letter": cover_letter
    }