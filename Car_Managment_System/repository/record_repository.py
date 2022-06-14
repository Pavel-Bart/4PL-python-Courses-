from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import models
import schemas


def create(request: schemas.CarBrandCreate, car_id: int, db: Session):
    new_record = models.MileageRecord(
        record=request.record,
        car_id=car_id
    )

    db.add(new_record)
    db.commit()
    db.refresh(new_record)

    return new_record
