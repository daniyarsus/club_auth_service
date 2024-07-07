import uuid

from injector import inject
from fastapi import HTTPException, status

from src.domain.auth.dto import LoginUserWithUsernameDTO, LoginUserWithEmailDTO, LoginUserWithPhoneDTO
from src.domain.auth.exceptions import *
from src.infrastructure.db.postgres_db.repositories import AbstractSQLUserRepository
from src.infrastructure.db.redis_db.repositories import AbstractRedisAuthRepository
from src.infrastructure.tokens.jwt.repositories import AbstractAuthJWTRepository

import src.infrastructure.tokens.jwt.settings as jwt_settings


class AuthenticateWithUsernameUseCase:
    @inject
    def __init__(
            self,
            sql_user_repository: AbstractSQLUserRepository,
            redis_auth_repository: AbstractRedisAuthRepository,
            auth_jwt_repository: AbstractAuthJWTRepository
    ) -> None:
        self.sql_user_repository = sql_user_repository
        self.redis_auth_repository = redis_auth_repository
        self.auth_jwt_repository = auth_jwt_repository

    async def __call__(
            self,
            dto: LoginUserWithUsernameDTO
    ):
        try:
            existing_user = await self.sql_user_repository.get_one(
                username=dto.username
            )
            if existing_user:
                if existing_user.is_verified:
                    if existing_user.password == dto.password:
                        data = {
                            "user_id": existing_user.id,
                            "email": existing_user.email,
                            "phone": existing_user.phone,
                            "username": existing_user.username,
                            "session_id": str(uuid.uuid4())
                        }
                        access_token = await self.auth_jwt_repository.encode_token(
                            token_type="access",
                            data=data
                        )
                        refresh_token = await self.auth_jwt_repository.encode_token(
                            token_type="refresh",
                            data=data
                        )
                        await self.redis_auth_repository.set_one(
                            key="refresh_token",
                            value=refresh_token,
                            time_in_sec=getattr(jwt_settings, "JWT_REFRESH_TOKEN_EXPIRE_SECONDS")
                        )
                        return {"access_token": access_token, "refresh_token": refresh_token}
                    else:
                        raise HTTPException(
                            status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Incorrect username or password!'
                        )
                else:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail='User not verified!'
                    )
            else:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="User not found!"
                )
        except BaseException as exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(exception)
            )


class AuthenticateWithEmailUseCase:
    @inject
    def __init__(
            self,
            sql_user_repository: AbstractSQLUserRepository,
            redis_auth_repository: AbstractRedisAuthRepository,
            auth_jwt_repository: AbstractAuthJWTRepository
    ) -> None:
        self.sql_user_repository = sql_user_repository
        self.redis_auth_repository = redis_auth_repository
        self.auth_jwt_repository = auth_jwt_repository

    async def __call__(
            self,
            dto: LoginUserWithEmailDTO
    ):
        try:
            existing_user = await self.sql_user_repository.get_one(
                email=dto.email
            )
            if existing_user:
                if existing_user.is_verified:
                    if existing_user.password == dto.password:
                        data = {
                            "user_id": existing_user.id,
                            "email": existing_user.email,
                            "phone": existing_user.phone,
                            "username": existing_user.username,
                            "session_id": str(uuid.uuid4())
                        }
                        access_token = await self.auth_jwt_repository.encode_token(
                            token_type="access",
                            data=data
                        )
                        refresh_token = await self.auth_jwt_repository.encode_token(
                            token_type="refresh",
                            data=data
                        )
                        await self.redis_auth_repository.set_one(
                            key="refresh_token",
                            value=refresh_token,
                            time_in_sec=getattr(jwt_settings, "JWT_REFRESH_TOKEN_EXPIRE_SECONDS")
                        )
                        return {"access_token": access_token, "refresh_token": refresh_token}
                    else:
                        raise HTTPException(
                            status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Incorrect email or password!'
                        )
                else:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail='User not verified!'
                    )
            else:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="User not found!"
                )
        except BaseException as exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(exception)
            )


class AuthenticateWithPhoneUseCase:
    @inject
    def __init__(
            self,
            sql_user_repository: AbstractSQLUserRepository,
            redis_auth_repository: AbstractRedisAuthRepository,
            auth_jwt_repository: AbstractAuthJWTRepository
    ) -> None:
        self.sql_user_repository = sql_user_repository
        self.redis_auth_repository = redis_auth_repository
        self.auth_jwt_repository = auth_jwt_repository

    async def __call__(
            self,
            dto: LoginUserWithPhoneDTO
    ):
        try:
            existing_user = await self.sql_user_repository.get_one(
                phone=dto.phone
            )
            if existing_user:
                if existing_user.is_verified:
                    if existing_user.password == dto.password:
                        data = {
                            "user_id": existing_user.id,
                            "email": existing_user.email,
                            "phone": existing_user.phone,
                            "username": existing_user.username,
                            "session_id": str(uuid.uuid4())
                        }
                        access_token = await self.auth_jwt_repository.encode_token(
                            token_type="access",
                            data=data
                        )
                        refresh_token = await self.auth_jwt_repository.encode_token(
                            token_type="refresh",
                            data=data
                        )
                        await self.redis_auth_repository.set_one(
                            key="refresh_token",
                            value=refresh_token,
                            time_in_sec=getattr(jwt_settings, "JWT_REFRESH_TOKEN_EXPIRE_SECONDS")
                        )
                        return {"access_token": access_token, "refresh_token": refresh_token}
                    else:
                        raise HTTPException(
                            status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Incorrect phone or password!'
                        )
                else:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail='User not verified!'
                    )
            else:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="User not found!"
                )
        except BaseException as exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(exception)
            )
