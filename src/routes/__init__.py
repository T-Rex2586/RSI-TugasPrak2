from fastapi import APIRouter
from src.routes.event import router as event_router

api_router = APIRouter()

api_router.include_router(event_router)