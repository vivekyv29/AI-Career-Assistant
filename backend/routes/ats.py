from fastapi import APIRouter, UploadFile, File, Form
from services.chatbot_service import ask_ollama
from services.parser import extract_text
from utils.ats_scoring import calculate_ats_score

import os
import shutil

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/ats")
async def ats_score(
    job_description: str = Form(None),
    resume_text: str = Form(None),
    file: UploadFile = File(None)
):

    print("JOB DESCRIPTION =", job_description)
    print("RESUME TEXT =", resume_text)
    print("FILE =", file)

    if not job_description:
        return {
            "analysis": "Please enter a Job Description."
        }

    if file:

        file_path = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer
            )

        resume_text = extract_text(
            file_path
        )

    if not resume_text:
        return {
            "analysis": "Resume text not found."
        }

    scores = calculate_ats_score(
        resume_text,
        job_description
    )

    ats_score = scores["ats_score"]
    matched = scores["matched"]
    missing = scores["missing"]

    prompt = f"""
You are an ATS Resume Expert.

ATS Score: {ats_score}/100

Matched Skills:
{', '.join(matched[:30])}

Missing Skills:
{', '.join(missing[:30])}

Provide:

1. Strengths
2. Weaknesses
3. Resume Improvements
4. Final Verdict

Keep response concise.
"""

    ai_analysis = ask_ollama(prompt)

    return {
        "ats_score": ats_score,
        "keyword_score": scores["keyword_score"],
        "skills_score": scores["skills_score"],
        "experience_score": scores["experience_score"],
        "education_score": scores["education_score"],
        "matched_skills": matched,
        "missing_skills": missing,
        "analysis": ai_analysis
    }