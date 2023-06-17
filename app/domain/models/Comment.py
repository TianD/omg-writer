from datetime import datetime

from sqlalchemy import Column, Integer, Text, DateTime

from data.database import Base


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    chapter_id = Column(Integer)
    user_id = Column(Integer)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

