from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    year: datetime
    study_year: datetime

    math_AVG: float
    angl_AVG: float
    lt_AVG: float
    inf_AVG: float


class BossCreate(BaseModel):
    first_name: str
    last_name: str


class ClassCreate(BaseModel):
    title: str


class StudentAll(BaseModel):
    id: int
    first_name: str
    last_name: str
    year: datetime
    study_year: datetime

    class Config:
        orm_mode = True


class BossAll(BaseModel):
    id: int
    first_name: str
    last_name: str
    students: List[StudentAll] = []

    class Config:
        orm_mode = True






