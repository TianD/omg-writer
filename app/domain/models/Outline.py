from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from data.database import Base



class Outline(Base):
    __tablename__ = 'outlines'

    id = Column(Integer, primary_key=True)
    theme_id = Column(Integer)
    title = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


