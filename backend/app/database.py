# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL 연결 정보
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:0000@localhost:5432/postgres"  # 🔧 수정 필요

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# 📌 get_db 함수 정의
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
