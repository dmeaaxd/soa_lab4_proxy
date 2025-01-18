from fastapi import FastAPI

from app.routes.killers import killers_router

app = FastAPI()

app.include_router(killers_router, prefix="/killer", tags=["killer"])


