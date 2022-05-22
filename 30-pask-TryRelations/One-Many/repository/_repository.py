from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import models
import schemas


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user_by_id(id: int, db: Session):
    return db.query(models.User).filter(models.User.id == id).first()


def create_user(request: schemas.UserCreate, db: Session):
    new_user = models.User(
        email=request.email,
        passw=request.passw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    new_item = models.Item(**item.dict(), owner_id=user_id)

    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item
