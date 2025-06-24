from fastapi import APIRouter

from .stand_bies.router import router as stand_bies_router
from .sub_types.router import router as sub_types_router

api_routers = APIRouter()

api_routers.include_router(
    stand_bies_router,
    tags=["StandBies"],
    prefix="/stand_bies",
)

api_routers.include_router(
    sub_types_router,
    tags=["SubTypes"],
    prefix="/sub_types",
)