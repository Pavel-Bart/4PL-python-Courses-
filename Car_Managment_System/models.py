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

