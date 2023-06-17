import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

from dotenv import load_dotenv

load_dotenv('../configs/.env')

# 配置数据库连接
DATABASE_URL = "postgresql://postgres:123456@localhost:5432/omg-writer"
# 创建数据库引擎
engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)
# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata = MetaData()

Base = declarative_base(metadata=metadata)


def get_db() -> SessionLocal:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

