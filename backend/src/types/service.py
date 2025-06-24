import uuid

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.types.dao import TypeDAO
from src.types.models import TypeModel


class TypeService:
    @classmethod
    async def get_list(cls, session: AsyncSession):
        return await TypeDAO.find_all(session, limit=None, order_by="sequence")

    @classmethod
    async def get_by_id(cls, session: AsyncSession, type_id: uuid.UUID):
        type = await TypeDAO.find_one_or_none(session, TypeModel.id == type_id)
        if not type:
            raise HTTPException(status_code=404, detail="Type not found")
        return type