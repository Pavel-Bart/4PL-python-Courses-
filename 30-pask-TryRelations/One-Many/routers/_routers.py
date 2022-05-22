from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from typing import List
import models
import schemas
from repository import _repository as repo


router = APIRouter(
    prefix='/api/UserItems',
    tags=["UserItems"]
)


@router.post("/user/", response_model=schemas.UserSchema)
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    return repo.create_user(request, db)


@router.get("/users/", response_model=list[schemas.UserSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = repo.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/user/{user_id}", response_model=schemas.UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = repo.get_user_by_id(user_id, db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/{user_id}/items/", response_model=schemas.ItemSchema)
def create_item_for_user(user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return repo.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items/", response_model=list[schemas.ItemSchema])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = repo.get_items(db, skip=skip, limit=limit)
    return items

