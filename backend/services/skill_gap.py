from fastapi import APIRouter
from pydantic import BaseModel
from services.chatbot_service import ask_ollama
router = APIRouter()

class SkillGapRequest(BaseModel):
    skills: list[str]
    role: str

@router.post("/skill-gap")
def skill_gap(request: SkillGapRequest):

    prompt = f"""
You are an expert career advisor.

Current Skills:
{', '.join(request.skills)}

Target Career:
{request.role}

Provide:

1. Missing Skills
2. Learning Priority
3. Recommended Projects
4. Estimated Time To Become Job Ready

Return plain text only.
Do NOT use markdown.
Do NOT use ** or ##.
Use bullet points.
"""

    result = ask_ollama(prompt)

    return {
        "analysis": result
    }