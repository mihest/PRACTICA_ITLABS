import uuid

from sqlalchemy import UUID, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import Base


class StandBiesModel(Base):
    __tablename__ = "stand_bies"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    media: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    sequence: Mapped[int] = mapped_column(Integer, nullable=False)

