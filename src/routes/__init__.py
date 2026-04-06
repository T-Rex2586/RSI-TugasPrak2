from fastapi import APIRouter
from src.routes.event_route import router as event_router
from src.routes.user_route import router as user_router

api_router = APIRouter()

api_router.include_router(event_router)
api_router.include_router(user_router)