from fastapi import FastAPI
from database import engine
from routers import product_routers, category_routers
import models

app = FastAPI()
app.include_router(product_routers.router)
app.include_router(category_routers.router)

models.Base.metadata.create_all(engine)
