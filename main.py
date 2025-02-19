from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database import models
from database.database import engine
from routers import user, post, comments
from auth import authentication

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(comments.router)
app.include_router(authentication.router)

models.Base.metadata.create_all(engine)

app.mount("/images", StaticFiles(directory = "images"), name="images")