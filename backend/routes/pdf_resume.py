from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import FileResponse

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

router = APIRouter()

class PDFRequest(BaseModel):
    resume_text: str


@router.post("/download-resume-pdf")
def download_resume_pdf(request: PDFRequest):

    pdf_file = "optimized_resume.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    heading_style = ParagraphStyle(
        "Heading",
        parent=styles["Heading2"],
        spaceAfter=10,
    )

    body_style = styles["BodyText"]

    content = []

    lines = request.resume_text.split("\n")

    headings = [
        "CONTACT INFORMATION",
        "PROFESSIONAL SUMMARY",
        "EDUCATION",
        "TECHNICAL SKILLS",
        "PROJECTS",
        "CERTIFICATIONS",
        "ACHIEVEMENTS",
    ]

    for line in lines:

        line = line.replace("**", "").strip()

        if not line:
            continue

        if line.upper() in headings:

            content.append(
                Paragraph(line, heading_style)
            )

            content.append(
                Spacer(1, 8)
            )

        else:

            content.append(
                Paragraph(line, body_style)
            )

            content.append(
                Spacer(1, 3)
            )

    doc.build(content)

    return FileResponse(
        pdf_file,
        filename="optimized_resume.pdf",
        media_type="application/pdf"
    )