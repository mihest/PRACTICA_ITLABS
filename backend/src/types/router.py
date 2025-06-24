import uuid

from fastapi import APIRouter

from src.database import SessionDep
from src.types.schemas import TypeResponse
from src.types.service import TypeService

router = APIRouter()


@router.get("")
async def get_list(
        session: SessionDep
) -> list[TypeResponse]:
    return await TypeService.get_list(session)


@router.get("/{type_id}")
async def get_by_id(
        type_id: uuid.UUID,
        session: SessionDep
) -> TypeResponse:
    return await TypeService.get_by_id(session, type_id)