from fastapi import FastAPI
from database import models
from database.database import engine
from routers import user

app = FastAPI()

app.include_router(user.router)

@app.get("/")
def get_it():
    return "THi si sfun"

models.Base.metadata.create_all(engine)