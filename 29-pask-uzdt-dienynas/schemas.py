from pydantic import BaseModel


class HumanShortGetInfoSchema(BaseModel):
    first_name: str
    last_name: str
    MathAvg: float

    class Config:
        orm_mode = True


class StudentPostSchema(BaseModel):
    first_name: str
    last_name: str
    MathAvg: float
    LtAvg: float
    EnglishAvg: float
    ProgrammingAvg: float

