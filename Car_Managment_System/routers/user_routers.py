from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from typing import List
import models
import schemas
#from repository import _repository as repo

router = APIRouter(
    prefix='/api/user',
    tags=['Users']
)

@router.post('/userCreate')
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):

    new_settings = models.UserSettings(
        Consumption=request.settings.Consumption,
        Odometer=request.settings.Odometer
    )
    db.add(new_settings)
    db.commit()
    db.refresh(new_settings)

    new_user = models.User(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        settings_id=new_settings.id,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get('/getAll1', response_model=List[schemas.UserAll])
def all(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@router.get('/getAll2')
def all_users(db: Session = Depends(get_db)):

    return db.query(models.User) \
        .join(models.UserSettings).options(selectinload(models.User.settings)).all()
