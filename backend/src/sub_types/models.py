import uuid

from sqlalchemy import UUID, String, Integer, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.documents.models import DocumentModel
from src.models import Base


class SubTypeModel(Base):
    __tablename__ = "sub_types"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    title: Mapped[String] = mapped_column(String, nullable=False)
    image: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    sequence: Mapped[int] = mapped_column(Integer, nullable=False)
    type_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey('types.id', ondelete='CASCADE', onupdate='CASCADE'),
        nullable=False
    )

    type: Mapped["TypeModel"] = relationship(
        "TypeModel",
        back_populates="sub_types"
    )
    documents: Mapped[list[DocumentModel]] = relationship(
        "DocumentModel",
        back_populates="sub_type",
        lazy="joined"
    )


