from sqlalchemy.ext.asyncio import AsyncSession

from src.stand_bies.dao import StandBiesDAO


class StandBiesService:
    @classmethod
    async def get_all(cls, session: AsyncSession):
        return await StandBiesDAO.find_all(
            session,
            limit=None,
            order_by="sequence"
        )