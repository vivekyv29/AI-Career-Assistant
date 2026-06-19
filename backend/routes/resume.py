from fastapi import APIRouter, UploadFile, File
from services.skill_extractor import extract_skills
from services.parser import extract_text
from fastapi import Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal
from database.dependency import get_db

from models.resume import Resume
from utils.auth_dependency import (
    get_current_user
)
from sqlalchemy.orm import Session
from database.dependency import get_db
from models.resume import Resume

import os
import shutil

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)
@router.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...),
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

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

    skills = extract_skills(
        resume_text
    )

    resume = Resume(
        user_id=user["user_id"],
        filename=file.filename,
        skills=",".join(skills),
        resume_text=resume_text
    )

    db.add(resume)
    db.commit()
    db.refresh(resume)

    return {
        "user": user["email"],
        "filename": file.filename,
        "skills": skills
    }
@router.get("/my-resumes")
def my_resumes(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    resumes = db.query(Resume).filter(
        Resume.user_id == user["user_id"]
    ).all()

    return resumes

@router.get("/latest-resume")
def latest_resume(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    resume = (
        db.query(Resume)
        .filter(
            Resume.user_id == user["user_id"]
        )
        .order_by(Resume.id.desc())
        .first()
    )

    if not resume:
        return {
            "resume_text": ""
        }

    return {
        "resume_text": resume.resume_text
    }
@router.get("/latest-resume-skills")
def latest_resume_skills(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    resume = (
        db.query(Resume)
        .filter(
            Resume.user_id == user["user_id"]
        )
        .order_by(Resume.id.desc())
        .first()
    )

    if not resume:
        return {
            "skills": []
        }

    return {
        "skills": resume.skills.split(",")
    }
    


