import uuid

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.documents.schemas import DocumentResponse
from src.sub_types.dao import SubTypeDAO
from src.sub_types.models import SubTypeModel
from src.sub_types.schemas import SubTypeResponse
from src.videos.schemas import VideoResponse


class SubTypeService:
    @classmethod
    async def get_by_id(cls, session: AsyncSession, sub_type_id: uuid.UUID):
        sub_type = await SubTypeDAO.find_one_or_none(session, SubTypeModel.id == sub_type_id)
        if not sub_type:
            raise HTTPException(status_code=404, detail="Subtype not found")
        return sub_type
