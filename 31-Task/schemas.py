from typing import List
from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str


class CategoryCreate(BaseModel):
    title: str


class ProductAll(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CategoryAll(BaseModel):
    id: int
    title: str
    product: List[ProductAll] = []

    class Config:
        orm_mode = True
