from sqlalchemy import Column, Integer, String

from database.db import Base

class Progress(Base):
    __tablename__ = "progress"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(Integer)

    role = Column(String)

    step = Column(String)

    completed = Column(
        Integer,
        default=0
    )