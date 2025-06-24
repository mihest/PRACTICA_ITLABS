from src.dao import BaseDAO
from src.stand_bies.models import StandBiesModel


class StandBiesDAO(BaseDAO[StandBiesModel, None, None]):
    model = StandBiesModel