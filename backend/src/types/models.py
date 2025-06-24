import uuid

from sqlalchemy import UUID, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import Base
from src.sub_types.models import SubTypeModel


class TypeModel(Base):
    __tablename__ = "types"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    title: Mapped[str] = mapped_column(String, nullable=False)
    image: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    sequence: Mapped[int] = mapped_column(Integer, nullable=False)

    sub_types: Mapped[list[SubTypeModel]] = relationship(
        "SubTypeModel",
        back_populates="type",
        order_by="SubTypeModel.sequence"
    )




