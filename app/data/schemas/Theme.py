# coding: utf-8
# Copyright (c) OMG-WRITER (2023)
# Author: TianD (huiguoyu)

from pydantic import BaseModel

class Theme(BaseModel):

    title: str

    class Config:
        orm_mode = True