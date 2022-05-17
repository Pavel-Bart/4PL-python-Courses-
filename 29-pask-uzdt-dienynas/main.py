from fastapi import FastAPI
from database import engine
from routers import student_routers
import models

app = FastAPI()

app.include_router(student_routers.router)
models.Base.metadata.create_all(engine)
