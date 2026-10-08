from fastapi import FastAPI

from src.routers.health_check_router import router as health_check_router

app = FastAPI()

app.include_router(health_check_router)
