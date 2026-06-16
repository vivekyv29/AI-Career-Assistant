from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func

from database.base import Base

class MockInterview(Base):
    __tablename__ = "mock_interviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    role = Column(String(255))
    total_score = Column(Integer)
    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )