from fastapi import FastAPI
from database import engine
from routers import _routers
import models

app = FastAPI()

app.include_router(_routers.router)
models.Base.metadata.create_all(engine)


