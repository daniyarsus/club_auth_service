from typing import override, NoReturn

from injector import inject, singleton

from src.domain.auth.interfaces import LoginUserInterface
from src.domain.auth.dto import (
    LoginUserWithUsernameDTO,
    LoginUserWithEmailDTO,
    LoginUserWithPhoneDTO
)
from src.domain.auth.usecases import (
    AuthenticateWithUsernameUseCase,
    AuthenticateWithEmailUseCase,
    AuthenticateWithPhoneUseCase
)
from src.infrastructure.db.postgres_db.repositories import AbstractSQLUserRepository
from src.infrastructure.db.redis_db.repositories import AbstractRedisAuthRepository
from src.infrastructure.tokens.jwt.repositories import AbstractAuthJWTRepository


@singleton
class LoginUserService(LoginUserInterface):
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

    @override
    async def authenticate_with_username(self, dto: LoginUserWithUsernameDTO):
        use_case = AuthenticateWithUsernameUseCase(
            sql_user_repository=self.sql_user_repository,
            redis_auth_repository=self.redis_auth_repository,
            auth_jwt_repository=self.auth_jwt_repository
        )
        return await use_case(
            dto=dto
        )

    @override
    async def authenticate_with_email(self, dto: dict):
        use_case = AuthenticateWithEmailUseCase(
            sql_user_repository=self.sql_user_repository,
            redis_auth_repository=self.redis_auth_repository,
            auth_jwt_repository=self.auth_jwt_repository
        )
        return await use_case(
            dto=dto
        )

    @override
    async def authenticate_with_phone(self, dto: dict):
        use_case = AuthenticateWithPhoneUseCase(
            sql_user_repository=self.sql_user_repository,
            redis_auth_repository=self.redis_auth_repository,
            auth_jwt_repository=self.auth_jwt_repository
        )
        return await use_case(
            dto=dto
        )
