import uuid

from sqlalchemy import UUID, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import Base


class VideoModel(Base):
    __tablename__ = "videos"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    video: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    sequence: Mapped[int] = mapped_column(Integer, nullable=False)
    document_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey('documents.id', ondelete='CASCADE', onupdate='CASCADE'),
        nullable=False
    )

    document: Mapped['DocumentModel'] = relationship(
        'DocumentModel',
        back_populates="videos"
    )


