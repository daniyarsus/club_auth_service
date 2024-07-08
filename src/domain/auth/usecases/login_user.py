import uuid

from injector import inject
from fastapi import HTTPException, status

from src.domain.auth.dto import (
    LoginUserWithUsernameDTO,
    LoginUserWithEmailDTO,
    LoginUserWithPhoneDTO,
    GetRefreshTokenDTO
)
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
                        session_id = str(uuid.uuid4())
                        data = {
                            "user_id": existing_user.id,
                            "email": existing_user.email,
                            "phone": existing_user.phone,
                            "username": existing_user.username,
                            "session_id": session_id
                        }
                        access_token = await self.auth_jwt_repository.encode_token(
                            token_type="access",
                            data=data
                        )
                        refresh_token = await self.auth_jwt_repository.encode_token(
                            token_type="refresh",
                            data=data
                        )
                        token_set = await self.redis_auth_repository.set_one(
                            key=f"refresh_token_of_{session_id}",
                            value=refresh_token,
                            time_in_sec=getattr(jwt_settings, "JWT_REFRESH_TOKEN_EXPIRE_SECONDS")
                        )
                        if token_set:
                            return {"access_token": access_token, "refresh_token": refresh_token}
                        else:
                            raise HTTPException(
                                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail='Token not saved'
                            )
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
                        session_id = str(uuid.uuid4())
                        data = {
                            "user_id": existing_user.id,
                            "email": existing_user.email,
                            "phone": existing_user.phone,
                            "username": existing_user.username,
                            "session_id": session_id
                        }
                        access_token = await self.auth_jwt_repository.encode_token(
                            token_type="access",
                            data=data
                        )
                        refresh_token = await self.auth_jwt_repository.encode_token(
                            token_type="refresh",
                            data=data
                        )
                        token_set = await self.redis_auth_repository.set_one(
                            key=f"refresh_token_of_{session_id}",
                            value=refresh_token,
                            time_in_sec=getattr(jwt_settings, "JWT_REFRESH_TOKEN_EXPIRE_SECONDS")
                        )
                        if token_set:
                            print(session_id)

                            return {"access_token": access_token, "refresh_token": refresh_token}
                        else:
                            raise HTTPException(
                                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail='Token not saved'
                            )
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
                        session_id = str(uuid.uuid4())
                        data = {
                            "user_id": existing_user.id,
                            "email": existing_user.email,
                            "phone": existing_user.phone,
                            "username": existing_user.username,
                            "session_id": session_id
                        }
                        access_token = await self.auth_jwt_repository.encode_token(
                            token_type="access",
                            data=data
                        )
                        refresh_token = await self.auth_jwt_repository.encode_token(
                            token_type="refresh",
                            data=data
                        )
                        token_set = await self.redis_auth_repository.set_one(
                            key=f"refresh_token_of_{session_id}",
                            value=refresh_token,
                            time_in_sec=getattr(jwt_settings, "JWT_REFRESH_TOKEN_EXPIRE_SECONDS")
                        )
                        if token_set:
                            return {"access_token": access_token, "refresh_token": refresh_token}
                        else:
                            raise HTTPException(
                                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail='Token not saved'
                            )
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


class GetRefreshTokenUseCase:
    @inject
    def __init__(
            self,
            redis_auth_repository: AbstractRedisAuthRepository,
            auth_jwt_repository: AbstractAuthJWTRepository
    ) -> None:
        self.redis_auth_repository = redis_auth_repository
        self.auth_jwt_repository = auth_jwt_repository

    async def __call__(
            self,
            token: str
    ):
        try:
            payload: dict = await self.auth_jwt_repository.decode_token(
                token=token
            )
            session_id = payload.get('session_id')
            user_id = payload.get('user_id')
            email = payload.get('email')
            phone = payload.get('phone')
            username = payload.get('username')

            existing_token = await self.redis_auth_repository.get_one(
                key=f"refresh_token_of_{session_id}"
            )
            if existing_token:
                check_token_type = payload.get('type')
                if check_token_type == 'refresh':
                    data = {
                        "user_id": user_id,
                        "email": email,
                        "phone": phone,
                        "username": username,
                        "session_id": session_id,
                    }
                    access_token = await self.auth_jwt_repository.encode_token(
                        token_type='access',
                        data=data
                    )
                    return {
                        'access_token': access_token
                    }
                else:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail='Token type not allowed!'
                    )
            else:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail='Token not found!'
                )
        except BaseException as exception:
            #raise HTTPException(
            #    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            #    detail=str(exception)
            #)
            raise exception
