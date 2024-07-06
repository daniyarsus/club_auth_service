from injector import inject
from fastapi import HTTPException, status

from src.domain.auth.dto import (
    RegisterUserWithEmailDTO, VerifyUserWithEmailGetCodeDTO, VerifyUserWithEmailSetCodeDTO,
    RegisterUserWithPhoneDTO, VerifyUserWithPhoneGetCodeDTO, VerifyUserWithPhoneSetCodeDTO
)
from src.domain.auth.exceptions import *
from src.infrastructure.db.postgres_db.repositories import AbstractSQLUserRepository
from src.infrastructure.db.redis_db.repositories import AbstractRedisAuthRepository
from src.infrastructure.smtp.email.repositories import *
from src.infrastructure.smtp.sms.repositories import *


class RegisterUserWithEmailUseCase:
    def __init__(
            self,
            sql_user_repository: AbstractSQLUserRepository
    ) -> None:
        self.sql_user_repository = sql_user_repository

    async def __call__(
            self,
            dto: RegisterUserWithEmailDTO
    ):
        try:
            existing_user = await self.sql_user_repository.get_one(
                email=dto.email,
                username=dto.username,
            )
            if existing_user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Email already registered!'  # ToDo: изменить на свои статусы
                )
            else:
                result = await self.sql_user_repository.add_one(
                    email=dto.email,
                    username=dto.username,
                    password=dto.password
                )
        except BaseException as exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(exception)
            )
