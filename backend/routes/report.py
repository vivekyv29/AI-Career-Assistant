from fastapi import APIRouter
from fastapi.responses import FileResponse
from reportlab.pdfgen import canvas

router = APIRouter()

@router.get("/career-report")
def generate_report():

    file_name = "career_report.pdf"

    pdf = canvas.Canvas(file_name)

    pdf.setTitle("Career Report")

    pdf.drawString(
        100,
        800,
        "AI Career Assistant Report"
    )

    pdf.drawString(
        100,
        760,
        "Resume Score: 85/100"
    )

    pdf.drawString(
        100,
        730,
        "Skill Gap: Learn FastAPI and SQL"
    )

    pdf.drawString(
        100,
        700,
        "Interview Score: 8/10"
    )

    pdf.drawString(
        100,
        670,
        "Recommended Role: AI Engineer"
    )

    pdf.save()

    return {
        "message": "Report Generated Successfully"
    }


@router.get("/download-report")
def download_report():

    return FileResponse(
        "career_report.pdf",
        media_type="application/pdf",
        filename="career_report.pdf"
    )