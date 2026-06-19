from fastapi import APIRouter
from pydantic import BaseModel
from services.chatbot_service import ask_ollama

router = APIRouter()

class RoadmapRequest(BaseModel):
    role: str
    skills: list[str]

@router.post("/roadmap")
def roadmap(request: RoadmapRequest):

    prompt = f"""
You are an expert career mentor.

Current Skills:
{', '.join(request.skills)}

Target Role:
{request.role}

Create a personalized roadmap.

Include:

1. Missing Skills
2. Learning Order
3. Projects To Build
4. Estimated Timeline

Return roadmap steps only.
One step per line.
"""

    result = ask_ollama(prompt)

    roadmap_steps = []

    for line in result.split("\n"):
        line = line.strip()

        if line:
            roadmap_steps.append(line)

    return {
        "roadmap": roadmap_steps
    }