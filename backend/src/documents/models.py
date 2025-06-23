import uuid

from sqlalchemy import UUID, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import Base
from src.sub_types.models import SubTypeModel


class DocumentModel(Base):
    __tablename__ = "documents"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    title: Mapped[str] = mapped_column(String, nullable=False)
    media: Mapped[str] = mapped_column(String, unique=True, nullable=True)
    sequence: Mapped[int] = mapped_column(Integer, nullable=False)
    sub_type_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey('sub_types.id', ondelete='CASCADE', onupdate='CASCADE'),
        nullable=False
    )

    sub_type: Mapped[SubTypeModel] = relationship(
        'SubTypeModel',
        backref='documents',
    )
    videos: Mapped[list["VideoModel"]] = relationship(
        "VideoModel",
        back_populates="document"
    )


