from fastapi import FastAPI
from . import models
from .database import engine
from .routes import posts
from .routes import auth, comments, likes

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(posts.router)
app.include_router(comments.router)
app.include_router(likes.router)
