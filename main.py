from fastapi import FastAPI

import src.models as models

from src.database import engine

from src.routers.admin_router import router as admin_router
from src.routers.health_check_router import router as health_check_router

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(health_check_router)
app.include_router(admin_router)