from datetime import datetime

from sqlalchemy import Integer, String, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from .base import SQLAlchemyBase


class User(SQLAlchemyBase):
    __tablename__ = "user_table"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )

    email: Mapped[str] = mapped_column(
        String, index=True, unique=True, nullable=False
    )
    phone: Mapped[str] = mapped_column(
        String, index=True, unique=True, nullable=False
    )
    username: Mapped[str] = mapped_column(
        String, index=True, unique=True, nullable=False
    )
    password: Mapped[str] = mapped_column(
        String, nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=datetime.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True, onupdate=datetime.now()
    )
