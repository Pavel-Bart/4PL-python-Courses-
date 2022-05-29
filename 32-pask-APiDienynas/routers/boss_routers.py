from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from typing import List
import models
import schemas
#from repository import _repository as repo

router = APIRouter(
    prefix='/api/task',
    tags=['Boss']
)


@router.get('/boss', response_model=List[schemas.BossAll])
def all_students(db: Session = Depends(get_db)):
    return db.query(models.Boss).all()


@router.post('/create')
def create_boss(request: schemas.BossCreate, db: Session = Depends(get_db)):
    new_boss = models.Boss(
        first_name=request.first_name,
        last_name=request.last_name,
    )

    db.add(new_boss)
    db.commit()
    db.refresh(new_boss)

    return new_boss
