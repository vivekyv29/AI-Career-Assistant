from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SkillGapRequest(BaseModel):
    resume_skills: list
    target_role: str

ROLE_SKILLS = {
    "AI Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "Docker",
        "AWS"
    ],
    "Data Scientist": [
        "Python",
        "SQL",
        "Pandas",
        "NumPy",
        "Machine Learning",
        "Statistics"
    ]
}

@router.post("/skill-gap")
def skill_gap(request: SkillGapRequest):

    required = ROLE_SKILLS.get(
        request.target_role,
        []
    )

    matched = []

    missing = []

    for skill in required:

        if skill in request.resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    score = 0

    if len(required) > 0:
        score = round(
            len(matched) /
            len(required) * 100,
            2
        )

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "match_percentage": score
    }