# coding: utf-8
# Copyright (c) OMG-WRITER (2023)
# Author: TianD (huiguoyu)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from data.database import get_db
from data.schemas import Theme as ThemeSchema
from domain.models import Theme

router = APIRouter()

# 路由路径常量
PREFIX = "/themes"
TAGS = ["themes"]
CREATE_PATH = ""
FIND_PATH = ""
GET_PATH = "/{theme_id}"
UPDATE_PATH = "/{theme_id}"
DELETE_PATH = "/{theme_id}"


@router.post(CREATE_PATH, response_model=ThemeSchema)
def create_theme(theme: ThemeSchema, db: Session = Depends(get_db)):
    db_theme = Theme(name=theme.name)
    db.add(db_theme)
    db.commit()
    db.refresh(db_theme)
    return db_theme


@router.get(GET_PATH, response_model=ThemeSchema)
def get_theme(theme_id: int, db: Session = Depends(get_db)):
    db_theme = db.query(Theme).get(theme_id)
    if not db_theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    return db_theme


@router.get(FIND_PATH, response_model=ThemeSchema)
def find_theme(theme_name: str, db: Session = Depends(get_db)):
    db_themes = db.query(Theme).filter(Theme.name == theme_name).all()
    if not db_themes:
        return []
    return db_themes


@router.put(UPDATE_PATH, response_model=ThemeSchema)
def update_theme(theme_id: int, theme: ThemeSchema, db: Session = Depends(get_db)):
    db_theme = db.query(Theme).get(theme_id)
    if not db_theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    db_theme.name = theme.name
    db.commit()
    db.refresh(db_theme)
    return db_theme


@router.delete(DELETE_PATH)
def delete_theme(theme_id: int, db: Session = Depends(get_db)):
    db_theme = db.query(Theme).get(theme_id)
    if not db_theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    db.delete(db_theme)
    db.commit()
    return {"message": "Theme deleted"}
