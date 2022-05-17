from database import Base
from sqlalchemy import Column, Integer, String, Float


class Student(Base):
    __tablename__ = "Students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    LtAvg = Column(Float)
    MathAvg = Column(Float)
    EnglishAvg = Column(Float)
    ProgrammingAvg = Column(Float)

