# coding: utf-8
# Copyright (c) OMG-WRITER (2023)
# Author: TianD (huiguoyu)

from pydantic import BaseModel


class Chapter(BaseModel):
    name: str

    class Config:
        orm_mode = True
