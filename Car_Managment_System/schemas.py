from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class UserSettingsCreate(BaseModel):
    Consumption: float
    Odometer: float


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    settings: UserSettingsCreate


class SettingsAll(BaseModel):
    id: int
    Consumption: float
    Odometer: float

    class Config:
        orm_mode = True


class UserAll(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    settings: SettingsAll

    class Config:
        orm_mode = True

