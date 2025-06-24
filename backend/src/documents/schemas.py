import uuid

from pydantic import BaseModel

from src.videos.schemas import VideoResponse


class DocumentResponse(BaseModel):
    id: uuid.UUID
    media: str
    title: str
    sequence: int
    videos: list[VideoResponse]