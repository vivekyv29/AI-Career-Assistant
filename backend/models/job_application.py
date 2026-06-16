from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func

from database.base import Base

class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)

    company = Column(String(255))
    role = Column(String(255))
    status = Column(String(100))

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )