from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from typing import List
import models
import schemas
from repository import car_repository as repo

router = APIRouter(
    prefix='/api/car',
    tags=['Cars']
)


@router.post('/Create/{user_id}{brand_id}{model_id}')
def create_car(useer_id: int, brand_id: int, model_id: int, db: Session = Depends(get_db)):
    return repo.create(db, useer_id, brand_id, model_id)


@router.post('/Create/V2')
def create_car(request: schemas.CarCreate, db: Session = Depends(get_db)):
    return repo.createV2(request, db)


@router.get('/Get', response_model=List[schemas.CarAll])
def all(db: Session = Depends(get_db)):
    return repo.get_all(db)


@router.put('/Update/{id}')
def update(id: int, request: schemas.CarCreate, db: Session = Depends(get_db)):
    return repo.update(id, request, db)


@router.delete('/Delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return repo.delete(id, db)
