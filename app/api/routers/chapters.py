# coding: utf-8
# Copyright (c) OMG-WRITER (2023)
# Author: TianD (huiguoyu)

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from data.database import get_db
from data.schemas import Chapter as ChapterSchema
from domain.models import Chapter

router = APIRouter()

# 路由路径常量
PREFIX = "/chapters"
TAGS = ["chapters"]
CREATE_PATH = ""
FIND_PATH = ""
GET_PATH = "/{chapter_id}"
UPDATE_PATH = "/{chapter_id}"
DELETE_PATH = "/{chapter_id}"


@router.post(CREATE_PATH, response_model=ChapterSchema)
def create_chapter(chapter: ChapterSchema, db: Session = Depends(get_db)):
    db_chapter = Chapter(name=chapter.name)
    db.add(db_chapter)
    db.commit()
    db.refresh(db_chapter)
    return db_chapter


@router.get(GET_PATH, response_model=ChapterSchema)
def get_chapter(chapter_id: int, db: Session = Depends(get_db)):
    db_chapter = db.query(Chapter).get(chapter_id)
    if not db_chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return db_chapter


@router.get(FIND_PATH, response_model=ChapterSchema)
def find_chapter(chapter_name: str, db: Session = Depends(get_db)):
    db_chapters = db.query(Chapter).filter(Chapter.name == chapter_name).all()
    if not db_chapters:
        return []
    return db_chapters


@router.put(UPDATE_PATH, response_model=ChapterSchema)
def update_chapter(chapter_id: int, chapter: ChapterSchema, db: Session = Depends(get_db)):
    db_chapter = db.query(Chapter).get(chapter_id)
    if not db_chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    db_chapter.name = chapter.name
    db.commit()
    db.refresh(db_chapter)
    return db_chapter


@router.delete(DELETE_PATH)
def delete_chapter(chapter_id: int, db: Session = Depends(get_db)):
    db_chapter = db.query(Chapter).get(chapter_id)
    if not db_chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    db.delete(db_chapter)
    db.commit()
    return {"message": "Chapter deleted"}
