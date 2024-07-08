import random

from fastapi import HTTPException, status
from injector import inject

from src.domain.auth.dto import (RegisterUserWithEmailDTO,
                                 RegisterUserWithPhoneDTO,
                                 VerifyUserWithEmailGetCodeDTO,
                                 VerifyUserWithEmailSetCodeDTO,
                                 VerifyUserWithPhoneGetCodeDTO,
                                 VerifyUserWithPhoneSetCodeDTO)
from src.domain.auth.exceptions import *
from src.infrastructure.db.postgres_db.repositories import \
    AbstractSQLUserRepository
from src.infrastructure.db.redis_db.repositories import \
    AbstractRedisAuthRepository
from src.infrastructure.smtp.email.repositories import \
    AbstractAuthSMTPEmailRepository
from src.infrastructure.smtp.sms.repositories import *


class RegisterUserWithEmailUseCase:
    @inject
    def __init__(
            self,
            sql_user_repository: AbstractSQLUserRepository
    ) -> None:
        self.sql_user_repository = sql_user_repository

    async def __call__(
            self,
            dto: RegisterUserWithEmailDTO
    ) -> None:
        try:
            existing_user = await self.sql_user_repository.get_one(
                email=dto.email,
                username=dto.username
            )
            if existing_user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Email or Username already registered!'
                )
            else:
                await self.sql_user_repository.add_one(
                    email=dto.email,
                    username=dto.username,
                    password=dto.password
                )
        except Exception as exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(exception)
            )


class VerifyUserWithEmailGetCodeUseCase:
    @inject
    def __init__(
            self,
            sql_user_repository: AbstractSQLUserRepository,
            redis_auth_repository: AbstractRedisAuthRepository,
            auth_smtp_email_repository: AbstractAuthSMTPEmailRepository,
    ) -> None:
        self.sql_user_repository = sql_user_repository
        self.redis_auth_repository = redis_auth_repository
        self.auth_smtp_email_repository = auth_smtp_email_repository

    async def __call__(
            self,
            dto: VerifyUserWithEmailGetCodeDTO
    ) -> None:
        try:
            existing_user_with_email = await self.sql_user_repository.get_one(
                email=dto.email
            )
            if existing_user_with_email:
                if not existing_user_with_email.is_verified:
                    random_code = random.randint(a=111111, b=999999)
                    await self.auth_smtp_email_repository.send_message(
                        message=f"Verify code: {random_code}. Don't reply him to another!",
                        to=dto.email,
                        subject="Your verify code!"
                    )
                    await self.redis_auth_repository.set_one(
                        key=f"email_verify_token_of_{dto.email}",
                        value=f"{random_code}",
                        time_in_sec=120
                    )
                    return random_code
                else:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail='User already verified!'
                    )
            else:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='User not registered!'
                )
        except BaseException as exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(exception)
            )


class VerifyUserWithEmailSetCodeUseCase:
    @inject
    def __init__(
            self,
            sql_user_repository: AbstractSQLUserRepository,
            redis_auth_repository: AbstractRedisAuthRepository
    ) -> None:
        self.sql_user_repository = sql_user_repository
        self.redis_auth_repository = redis_auth_repository

    async def __call__(
            self,
            dto: VerifyUserWithEmailSetCodeDTO
    ) -> None:
        try:
            existing_user_with_email = await self.sql_user_repository.get_one(
                email=dto.email
            )
            if existing_user_with_email:
                if not existing_user_with_email.is_verified:
                    check_user_code = await self.redis_auth_repository.get_one(
                        key=f"email_verify_token_of_{dto.email}",
                    )
                    if check_user_code.decode('utf-8') == dto.code:
                        await self.sql_user_repository.edit_one(
                            {"is_verified": True},
                            email=dto.email
                        )
                        await self.redis_auth_repository.delete_one(
                            key=f"email_verify_token_of_{dto.email}"
                        )
                    else:
                        raise HTTPException(
                            status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Code is invalid!'
                        )
                else:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail='User already verified!'
                    )
            else:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='User not registered!'
                )
        except BaseException as exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(exception)
            )
