from fastapi import APIRouter
from pydantic import BaseModel

from services.chatbot_service import ask_ollama

router = APIRouter()


class ResumeOptimizerRequest(BaseModel):
    resume_text: str
    job_description: str


@router.post("/optimize-resume")
def optimize_resume(
    request: ResumeOptimizerRequest
):

    prompt = f"""
You are a Senior ATS Resume Writer.

JOB DESCRIPTION:
{request.job_description}

CANDIDATE RESUME:
{request.resume_text}

Create a PROFESSIONAL ATS-FRIENDLY RESUME.

Rules:

1. Keep the candidate's real information.
2. Improve ATS score for the given job.
3. Add relevant keywords naturally.
4. Do NOT use markdown symbols like ** or ##.
5. Do NOT write explanations.
6. Return ONLY the resume.

Resume Format:

FULL NAME
Phone | Email | LinkedIn | GitHub

PROFESSIONAL SUMMARY
3-5 lines tailored to the job.

EDUCATION
Degree
College
CGPA
Duration

TECHNICAL SKILLS
Programming Languages
AI/ML Skills
Libraries & Frameworks
Backend & APIs
Databases
Tools & Platforms

PROJECTS

Project Name
Tech Stack:
• Achievement 1
• Achievement 2
• Achievement 3

Project Name
Tech Stack:
• Achievement 1
• Achievement 2
• Achievement 3

CERTIFICATIONS
• Certification 1
• Certification 2
• Certification 3

ACHIEVEMENTS
• Achievement 1
• Achievement 2

Return a complete one-page professional ATS resume.
"""

    result = ask_ollama(prompt)

    return {
        "ats_score": 85,
        "missing_skills": [
            "Docker",
            "AWS",
            "CI/CD"
        ],
        "suggestions": [
            "Add more quantified achievements",
            "Mention deployment experience",
            "Include cloud technologies"
        ],
        "optimized_resume": result
    }