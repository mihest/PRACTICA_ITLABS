from sqlalchemy import MetaData, CheckConstraint
from sqlalchemy.orm import DeclarativeBase

metadata = MetaData()


class Base(DeclarativeBase):
    metadata = metadata

    __table_args__ = (
        CheckConstraint("sequence > 0", name="sequence_positive"),
    )