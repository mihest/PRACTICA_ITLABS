import uuid

from pydantic import BaseModel


class VideoResponse(BaseModel):
    id: uuid.UUID
    video: str
    sequence: int