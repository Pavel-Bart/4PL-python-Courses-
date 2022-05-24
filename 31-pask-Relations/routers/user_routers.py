from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from typing import List
import models
import schemas
#from repository import _repository as repo

router = APIRouter(
    prefix='/api/post',
    tags=['Users']
)


@router.get('/users', response_model=List[schemas.UserAll])
def all_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@router.post('/create')
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(
        email=request.email,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
