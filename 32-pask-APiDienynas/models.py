from database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DATE, Float, DateTime
from sqlalchemy.orm import relationship


class Class(Base):
    __tablename__ = 'class'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)

    student = relationship('Student', back_populates='class_')

    boss_id = Column(Integer, ForeignKey('boss.id'))
    boss = relationship('Boss', back_populates='class_')


class Boss(Base):
    __tablename__ = 'boss'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)

    student = relationship('Student', back_populates='boss')
    class_ = relationship('Class', back_populates='boss', uselist=False)


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    year = Column(DateTime)
    study_year = Column(DateTime)

    math_AVG = Column(Float)
    angl_AVG = Column(Float)
    lt_AVG = Column(Float)
    inf_AVG = Column(Float)

    boss_id = Column(Integer, ForeignKey('boss.id'))
    boss = relationship('Boss', back_populates='student')

    class_id = Column(Integer, ForeignKey('class.id'))
    class_ = relationship('Class', back_populates='student')

