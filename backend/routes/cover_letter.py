from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import FileResponse

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from services.chatbot_service import ask_ollama

router = APIRouter()


class CoverLetterRequest(BaseModel):
    resume_text: str
    job_description: str


class CoverLetterPDFRequest(BaseModel):
    cover_letter: str


@router.post("/generate-cover-letter")
def generate_cover_letter(
    request: CoverLetterRequest
):

    prompt = f"""
    You are an expert HR recruiter and professional cover letter writer.

    Using the resume and job description below, generate a COMPLETE professional cover letter.

    RESUME:
    {request.resume_text}

    JOB DESCRIPTION:
    {request.job_description}

    Rules:
    1. Use the candidate's actual name from the resume.
    2. Do NOT use placeholders like [Your Name], [Date], [Company Name].
    3. Do NOT write instructions.
    4. Write a real professional cover letter.
    5. Keep it 300-400 words.
    6. Make it ATS friendly.
    7. Mention relevant skills and projects from the resume.
    8. Return only the final cover letter.
    """

    result = ask_ollama(prompt)

    return {
        "cover_letter": result
    }


@router.post("/download-cover-letter-pdf")
def download_cover_letter_pdf(
    request: CoverLetterPDFRequest
):

    pdf_file = "cover_letter.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    content = []

    for line in request.cover_letter.split("\n"):

        if line.strip():

            content.append(
                Paragraph(
                    line,
                    styles["BodyText"]
                )
            )

            content.append(
                Spacer(1, 6)
            )

    doc.build(content)

    return FileResponse(
        pdf_file,
        filename="cover_letter.pdf",
        media_type="application/pdf"
    )