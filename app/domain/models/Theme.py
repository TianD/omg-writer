from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from data.database import Base



class Theme(Base):
    __tablename__ = 'themes'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
