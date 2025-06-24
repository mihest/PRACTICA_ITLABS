from fastapi import APIRouter

from src.database import SessionDep
from src.stand_bies.schemas import StandBiesResponse
from src.stand_bies.service import StandBiesService

router = APIRouter()


@router.get("")
async def get_list(
        session: SessionDep
) -> list[StandBiesResponse]:
    return await StandBiesService.get_all(session)