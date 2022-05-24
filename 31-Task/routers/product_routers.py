from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from typing import List
import models
import schemas
#from repository import _repository as repo

router = APIRouter(
    prefix='/api/category',
    tags=['Products']
)


@router.post('/create/{CATEGORY_id}')
def create_product(request: schemas.ProductCreate, category_id: int, db: Session = Depends(get_db)):

    new_product = models.Product(
        name=request.name,

        category_id=category_id
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

