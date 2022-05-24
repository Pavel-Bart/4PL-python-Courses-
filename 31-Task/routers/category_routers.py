from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from typing import List
import models
import schemas
#from repository import _repository as repo

router = APIRouter(
    prefix='/api/category',
    tags=['Categories']
)


@router.get('/categories', response_model=List[schemas.CategoryAll])
def all_categories(db: Session = Depends(get_db)):
    return db.query(models.Category).all()


@router.post('/create')
def create_category(request: schemas.CategoryCreate, db: Session = Depends(get_db)):
    new_category = models.Category(
        title=request.title,
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category

