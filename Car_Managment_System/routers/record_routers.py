from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from typing import List
import models
import schemas
from repository import record_repository as repo

router = APIRouter(
    prefix='/api/record',
    tags=['Records']
)


@router.post('/Create/{car_id}')
def create_record(request: schemas.RecordCreate, car_id: int, db: Session = Depends(get_db)):
    return repo.create(request, car_id, db)

