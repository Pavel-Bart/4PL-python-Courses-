from fastapi import FastAPI
from database import engine
from routers import user_routers
from routers import blog_routers
import models


app = FastAPI()
app.include_router(user_routers.router)
app.include_router(blog_routers.router)

models.Base.metadata.create_all(engine)

