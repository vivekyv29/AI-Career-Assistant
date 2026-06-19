from sqlalchemy import (
    Column,
    Integer,
    Text,
    TIMESTAMP,
    String
)

from sqlalchemy.sql import func

from database.base import Base


class InterviewHistory(Base):
    __tablename__ = "interview_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    from sqlalchemy import ForeignKey

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    role = Column(String(200))

    question = Column(Text)

    answer = Column(Text)

    score = Column(Integer)

    feedback = Column(Text)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )