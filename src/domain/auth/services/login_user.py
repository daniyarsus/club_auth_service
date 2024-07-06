from injector import inject, singleton

from src.domain.auth.interfaces import LoginUserInterface
from src.domain.auth.dto import (
    LoginUserWithUsernameDTO,
    LoginUserWithEmailDTO,
    LoginUserWithPhoneDTO
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
            jwt_auth_repository: AbstractAuthJWTRepository
    ) -> None:
        self.sql_user_repository = sql_user_repository
        self.redis_auth_repository = redis_auth_repository
        self.jwt_auth_repository = jwt_auth_repository
