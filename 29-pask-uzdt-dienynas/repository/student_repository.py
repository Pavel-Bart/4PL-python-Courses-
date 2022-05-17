from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import models
import schemas


def check(student, id):
    if not student.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id {id} not found"
        )


def get_all_users(db: Session):
    return db.query(models.Student).all()


def get_single_by_id(id: int, db: Session):
    student = db.query(models.Student).filter(models.Student.id == id)

    check(student, id)

    return student.first()


def update(id: int, request: schemas.StudentPostSchema, db: Session):
    student = db.query(models.Student).filter(models.Student.id == id)

    check(student, id)

    student.update(request.dict())
    db.commit()

    return student.first()


def delete(id: int, db: Session):
    student = db.query(models.Student).filter(models.Student.id == id)

    check(student, id)

    student.delete()
    db.commit()

    return {"details": "Success"}


def create(request: schemas.StudentPostSchema, db: Session):
    new_student = models.Student(
        first_name=request.first_name,
        last_name=request.last_name,
        LtAvg=request.LtAvg,
        MathAvg=request.MathAvg,
        EnglishAvg=request.EnglishAvg,
        ProgrammingAvg=request.ProgrammingAvg
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student
