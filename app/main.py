from fastapi import FastAPI

from app.db import Base, engine
from app.routes.tickets import router as tickets_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ticket API")

app.include_router(tickets_router)