from sqlalchemy import MetaData, CheckConstraint
from sqlalchemy.orm import DeclarativeBase

custom_metadata  = MetaData()


class Base(DeclarativeBase):
    metadata = custom_metadata
