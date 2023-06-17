from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime

from data.database import Base


class Chapter(Base):
    __tablename__ = 'chapters'

    id = Column(Integer, primary_key=True)
    outline_id = Column(Integer)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    author_id = Column(Integer)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

