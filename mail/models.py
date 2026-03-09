from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func
from .database import Base


class EmailLog(Base):
    __tablename__ = "email_logs"

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(Text)
    response = Column(Text)
    created_at = Column(DateTime, server_default=func.now())

