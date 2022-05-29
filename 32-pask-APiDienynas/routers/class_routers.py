from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from typing import List
import models
import schemas
#from repository import _repository as repo

router = APIRouter(
    prefix='/api/task',
    tags=['Class']
)


@router.post('/create/{boss_id}')
def create_class(request: schemas.ClassCreate, boss_id: int, db: Session = Depends(get_db)):

    new_class = models.Class(
        title=request.title,
        boss_id=boss_id,
    )
    db.add(new_class)
    db.commit()
    db.refresh(new_class)

    return new_class
