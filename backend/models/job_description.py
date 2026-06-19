from sqlalchemy import Column, Integer, Text
from database.base import Base

class JobDescription(Base):
    __tablename__ = "job_descriptions"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)