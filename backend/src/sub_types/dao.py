from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.dao import BaseDAO
from src.documents.models import DocumentModel
from src.sub_types.models import SubTypeModel


class SubTypeDAO(BaseDAO[SubTypeModel, None, None]):
    model = SubTypeModel

    @classmethod
    async def find_one_or_none(
            cls,
            session: AsyncSession,
            *filters,
            **filter_by
    ) -> Optional[SubTypeModel]:
        stmt = (
            select(cls.model)
            .options(
                selectinload(cls.model.documents)
                .selectinload(DocumentModel.videos)
            )
            .filter(*filters)
            .filter_by(**filter_by)
        )
        result = await session.execute(stmt)
        return result.scalars().one_or_none()
