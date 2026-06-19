from fastapi import APIRouter
from fastapi.responses import FileResponse

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

router = APIRouter()


@router.get("/download-interview-report")
def download_interview_report():

    file_name = "interview_report.pdf"

    doc = SimpleDocTemplate(file_name)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Mock Interview Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Interview Completed Successfully",
            styles["BodyText"]
        )
    )

    doc.build(content)

    return FileResponse(
        file_name,
        media_type="application/pdf",
        filename="interview_report.pdf"
    )