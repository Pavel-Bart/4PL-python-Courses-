from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import models
import schemas


def check(user, id):
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Car with id {id} not found"
        )


def create(db: Session, useer_id: int, brand_id: int, model_id: int):

    new_car = models.User(
        user_id=useer_id,
        brand_id=brand_id,
        model_id=model_id,
    )
    db.add(new_car)
    db.commit()
    db.refresh(new_car)

    return new_car


def createV2(request: schemas.CarCreate, db: Session):
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

    new_brand = models.CarBrand(
        brand_name=request.brand_name,
    )
    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)

    new_model = models.Model(
        model=request.model,
        brand_id=new_brand.id,
    )
    db.add(new_model)
    db.commit()
    db.refresh(new_model)

    new_car = models.Car(
        user_id=new_user.id,
        brand_id=new_brand.id,
        model_id=new_model.id,
    )
    db.add(new_car)
    db.commit()
    db.refresh(new_car)

    return new_car


def get_all(db: Session):
    return db.query(models.Car).all()


def update(id: int, request: schemas.CarAll, db: Session):
    car = db.query(models.Car).filter(models.Car.id == id)

    check(car, id)

    car.update(request.dict())
    db.commit()

    return car.first()


def delete(id: int, db: Session):
    car = db.query(models.Car).filter(models.Car.id == id)

    check(car, id)

    car.delete()
    db.commit()

    return {"details": "Success"}

