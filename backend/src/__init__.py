from fastapi import APIRouter

from .stand_bies.router import router as stand_bies_router

api_routers = APIRouter()

api_routers.include_router(
    stand_bies_router,
    tags=["StandBies"],
    prefix="/stand_bies",
)