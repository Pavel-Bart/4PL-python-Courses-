from database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DATE, Float, DateTime
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)

    email = Column(String, unique=True)

    settings_id = Column(Integer, ForeignKey('settings.id'))
    settings = relationship('UserSettings', back_populates='owner')


class UserSettings(Base):
    __tablename__ = "settings"
    id = Column(Integer, primary_key=True, index=True)
    Consumption = Column(Float)
    Odometer = Column(Float)

    owner = relationship('User', back_populates='settings', uselist=False)


class CarBrand(Base):
    __tablename__ = "brands"
    id = Column(Integer, primary_key=True, index=True)
    brand_name = Column(String)

    models = relationship('Model', back_populates='brand')


class Model(Base):
    __tablename__ = "models"
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String)

    brand_id = Column(Integer, ForeignKey("brands.id"))
    brand = relationship("CarBrand", back_populates="models")


