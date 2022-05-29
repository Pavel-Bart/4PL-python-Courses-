from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from typing import List
import models
import schemas
#from repository import _repository as repo

router = APIRouter(
    prefix='/api/task',
    tags=['Student']
)


@router.get('/students', response_model=List[schemas.StudentAll])
def all_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()


@router.post('/create/{boss_id}/{class_id}')
def create_student(request: schemas.StudentCreate, boss_id: int, class_id: int, db: Session = Depends(get_db)):
    new_student = models.Student(
        first_name=request.first_name,
        last_name=request.last_name,
        year=request.year,
        study_year=request.study_year,

        math_AVG=request.math_AVG,
        angl_AVG=request.angl_AVG,
        lt_AVG=request.lt_AVG,
        inf_AVG=request.inf_AVG,

        boss_id=boss_id,
        class_id=class_id,
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student

