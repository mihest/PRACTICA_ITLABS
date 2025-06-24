import uuid

from pydantic import BaseModel
from pydantic.v1 import PositiveInt


class StandBiesResponse(BaseModel):
    id: uuid.UUID
    media: str
    title: str
    sequence: int
