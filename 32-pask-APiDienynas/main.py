from fastapi import FastAPI
from database import engine
from routers import student_routers
from routers import class_routers
from routers import boss_routers
import models

app = FastAPI()
app.include_router(student_routers.router)
app.include_router(class_routers.router)
app.include_router(boss_routers.router)

models.Base.metadata.create_all(engine)
