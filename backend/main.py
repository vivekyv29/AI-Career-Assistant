from fastapi import FastAPI

from routes.resume import router as resume_router
from routes.skill_gap import router as skill_gap_router
from routes.interview import router as interview_router
from routes.roadmap import router as roadmap_router
from routes.chatbot import router as chatbot_router
from routes.auth import router as auth_router
from dotenv import load_dotenv
from routes.ats import router as ats_router
from fastapi.middleware.cors import CORSMiddleware
from routes.report import router as report_router
from routes.cover_letter import router as cover_letter_router
from routes.resume_feedback import router as feedback_router
from routes.job_recommendation import router as job_router
from routes.job_tracker import router as tracker_router

from routes.dashboard import router as dashboard_router
from routes.mock_interview import (
    router as mock_interview_router
)


load_dotenv()
app = FastAPI(
    title="AI Career Assistant",
    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(resume_router)
app.include_router(skill_gap_router)
app.include_router(dashboard_router)
app.include_router(interview_router)
app.include_router(roadmap_router)
app.include_router(chatbot_router)
app.include_router(tracker_router)
app.include_router(ats_router)
app.include_router(auth_router)
app.include_router(job_router)
app.include_router(feedback_router)
app.include_router(
    cover_letter_router
)
app.include_router(
    report_router
)
app.include_router(
    mock_interview_router
)
@app.get("/")
def home():
    return {
        "message": "AI Career Assistant Running"
    }