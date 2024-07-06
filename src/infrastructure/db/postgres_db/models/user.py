from datetime import datetime

from sqlalchemy import Integer, String, TIMESTAMP, Boolean
from sqlalchemy.orm import Mapped, mapped_column, validates
from sqlalchemy.exc import SQLAlchemyError

from .base import SQLAlchemyBase


class User(SQLAlchemyBase):
    __tablename__ = "user_table"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )

    email: Mapped[str] = mapped_column(
        String, index=True, unique=True, nullable=True
    )
    phone: Mapped[str] = mapped_column(
        String, index=True, unique=True, nullable=True
    )
    username: Mapped[str] = mapped_column(
        String, index=True, unique=True, nullable=False
    )
    password: Mapped[str] = mapped_column(
        String, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, index=True, default=False
    )

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=datetime.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True, onupdate=datetime.now()
    )

    @validates('email', 'phone')
    def validate_email_or_phone(self, key, value):
        if key == 'email' and not value and not self.phone:
            raise SQLAlchemyError("Either email or phone must be provided")
        if key == 'phone' and not value and not self.email:
            raise SQLAlchemyError("Either email or phone must be provided")
        return value
