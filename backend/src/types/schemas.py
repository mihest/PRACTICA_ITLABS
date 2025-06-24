import uuid

from pydantic import BaseModel, Field

from src.sub_types.schemas import SubTypeResponse


class TypeResponse(BaseModel):
    id: uuid.UUID
    title: str
    image: str
    description: str
    sub_types: list[SubTypeResponse] = Field(..., serialization_alias="subTypes")
    sequence: int
