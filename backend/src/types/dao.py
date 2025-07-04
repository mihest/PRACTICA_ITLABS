from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.dao import BaseDAO
from src.documents.models import DocumentModel
from src.sub_types.models import SubTypeModel
from src.types.models import TypeModel


class TypeDAO(BaseDAO[TypeModel, None, None]):
    model = TypeModel

    @classmethod
    async def find_one_or_none(
            cls,
            session: AsyncSession,
            *filters,
            **filter_by
    ) -> Optional[TypeModel]:
        stmt = (
            select(cls.model)
            .options(
                selectinload(cls.model.sub_types)
                .selectinload(SubTypeModel.documents)
                .selectinload(DocumentModel.videos)
            )
            .filter(*filters)
            .filter_by(**filter_by)
        )
        result = await session.execute(stmt)
        return result.scalars().one_or_none()

    @classmethod
    async def find_all(
            cls,
            session: AsyncSession,
            *filters,
            offset: int = 0,
            limit: int = 100,
            order_by: str = None,
            **filter_by,
    ):
        stmt = (
            select(cls.model)
            .options(
                selectinload(TypeModel.sub_types)
                .selectinload(SubTypeModel.documents)
                .selectinload(DocumentModel.videos)
            )
            .filter(*filters)
            .filter_by(**filter_by)
            .offset(offset)
            .limit(limit)
            .order_by(order_by)
        )
        result = await session.execute(stmt)
        return result.scalars().all()
