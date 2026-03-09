from fastapi import FastAPI
from .database import engine
from .import models
from .routers import mail

app = FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(mail.router)
