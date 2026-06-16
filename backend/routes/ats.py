from fastapi import APIRouter, UploadFile, File, Form
from services.chatbot_service import ask_gemini
from services.parser import extract_text
import os
import shutil

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/ats")
async def ats_score(
    resume_text: str = Form(None),
    file: UploadFile = File(None)
):

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

        resume_text = extract_text(file_path)

    prompt = f"""
    Analyze this resume and provide:

    1. ATS Score out of 100
    2. Strengths
    3. Weaknesses
    4. Improvement Suggestions

    Resume:
    {resume_text}
    """

    result = ask_gemini(prompt)

    return {
        "analysis": result
    }