import uuid

from pydantic import BaseModel

from src.documents.schemas import DocumentResponse


class SubTypeResponse(BaseModel):
    id: uuid.UUID
    image: str
    title: str
    documents: list[DocumentResponse]
    sequence: int
