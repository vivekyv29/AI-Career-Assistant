from database.db import engine
from database.base import Base
from models.job_application import JobApplication
from models.user import User
from models.resume import Resume
from models.interview_history import InterviewHistory
from models.mock_interview import MockInterview

Base.metadata.create_all(
    bind=engine
)

print("Tables Created Successfully")