from fastapi import APIRouter
from fastapi.responses import FileResponse
from reportlab.pdfgen import canvas
# from backend.models import user
# from backend.database import db
from database.db import SessionLocal
from fastapi import Depends
from utils.auth_dependency import get_current_user
from models.resume import Resume
from models.interview_history import InterviewHistory
from services.chatbot_service import ask_ollama
router = APIRouter()

@router.get("/career-report")
def generate_report(
    user=Depends(get_current_user)
):

    file_name = "career_report.pdf"

    pdf = canvas.Canvas(file_name)


    db = SessionLocal()

    resume = db.query(
        Resume
    ).filter(
        Resume.user_id ==
        user["user_id"]
    ).first()

    interviews = db.query(
        InterviewHistory
    ).filter(
        InterviewHistory.user_id ==
        user["user_id"]
    ).all()

    skills = []

    if resume and resume.skills:
        skills = resume.skills.split(",")

    avg_interview = 0

    if interviews:
        avg_interview = round(
            sum(i.score for i in interviews)
            / len(interviews),
            1
        )

    prompt = f"""
    You are a career advisor.

    Current Skills:
    {', '.join(skills)}

    Return ONLY plain text.

    Rules:
    - Do not use markdown
    - Do not use **
    - Do not use #
    - Do not use headings
    - Use '-' for bullet points only
    - Maximum 10 lines

    Provide:
    - Missing Skills
    - Recommended Job Roles
    - Career Advice
    """

    ai_result = ask_ollama(prompt)

    pdf.setTitle("Career Report")

    y = 800

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(
        180,
        y,
        "AI Career Report"
    )

    y -= 50

    pdf.setFont("Helvetica", 12)

    report_lines = [
        "Career Report",
        "",
        "Detected Skills:"
    ]

    for skill in skills:
        report_lines.append(f"- {skill}")

    report_lines.append("")
    report_lines.append(
        f"Average Interview Score: {avg_interview}"
    )

    report_lines.append("")
    report_lines.append(
        "AI Recommendations:"
    )

    for line in ai_result.split("\n"):
        report_lines.append(line)


    for line in report_lines:

        if y < 80:
            pdf.showPage()
            y = 800
            pdf.setFont("Helvetica", 12)

        pdf.drawString(
            80,
            y,
            str(line)
        )

        y -= 20

    pdf.save()
    db.close()
    return {
        "message": "Career Report Generated Successfully",
        "skills": skills,
        "interview_score": avg_interview,
        "ai_recommendation": ai_result
    }


@router.get("/download-report")
def download_report():

    return FileResponse(
        "career_report.pdf",
        media_type="application/pdf",
        filename="career_report.pdf"
    )