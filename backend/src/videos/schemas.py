import uuid

from pydantic import BaseModel, ConfigDict


class VideoResponse(BaseModel):
    id: uuid.UUID
    video: str
    sequence: int
