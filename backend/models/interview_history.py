from sqlalchemy import Column, Integer, Text, TIMESTAMP
from sqlalchemy.sql import func

from database.base import Base

class InterviewHistory(Base):
    __tablename__ = "interview_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    question = Column(Text)
    answer = Column(Text)
    score = Column(Integer)
    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )