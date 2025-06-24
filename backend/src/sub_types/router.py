import uuid

from fastapi import APIRouter

from src.database import SessionDep
from src.sub_types.schemas import SubTypeResponse
from src.sub_types.service import SubTypeService

router = APIRouter()


@router.get("/{sub_type_id}")
async def get_by_id(
        sub_type_id: uuid.UUID,
        session: SessionDep
) -> SubTypeResponse:
    return await SubTypeService.get_by_id(session, sub_type_id)
