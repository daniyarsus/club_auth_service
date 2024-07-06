from typing import override

from injector import inject, singleton
from redis.client import AbstractRedis

from src.domain.auth.interfaces import RegisterUserInterface
from src.domain.auth.dto import (
    RegisterUserWithEmailDTO, VerifyUserWithEmailGetCodeDTO, VerifyUserWithEmailSetCodeDTO, RegisterUserWithPhoneDTO,
    VerifyUserWithPhoneSetCodeDTO
)
from src.domain.auth.usecases import (
    RegisterUserWithEmailUseCase, VerifyUserWithEmailGetCodeUseCase, VerifyUserWithEmailSetCodeUseCase
)
from src.infrastructure.db.postgres_db.repositories import (
    AbstractSQLUserRepository
)


@singleton
class RegisterUserService(RegisterUserInterface):
    @inject
    def __init__(
            self,
            sql_user_repository: AbstractSQLUserRepository,
            redis_auth_repository: AbstractSQLUserRepository
    ) -> None:
        self.sql_user_repository = sql_user_repository
        self.redis_auth_repository = redis_auth_repository

    @override
    async def register_user_with_email(self, dto: RegisterUserWithEmailDTO):
        use_case = RegisterUserWithEmailUseCase(
            sql_user_repository=self.sql_user_repository,
            redis_auth_repository=self.redis_auth_repository
        )
        return await use_case(
            dto=dto
        )

    @override
    async def get_email_code_verify_user(self, dto: VerifyUserWithEmailGetCodeDTO):
        use_case = VerifyUserWithEmailGetCodeUseCase(
            sql_user_repository=self.sql_user_repository,
            redis_auth_repository=self.redis_auth_repository
        )
        return await use_case(
            dto=dto
        )

    @override
    async def set_email_code_verify_user(self, dto: VerifyUserWithEmailSetCodeDTO):
        use_case = VerifyUserWithEmailSetCodeUseCase(
            sql_user_repository=self.sql_user_repository,
            redis_auth_repository=self.redis_auth_repository
        )
        return await use_case(
            dto=dto
        )

    @override
    async def register_user_with_phone(self, dto: RegisterUserWithPhoneDTO):
        pass

    @override
    async def get_phone_code_verify_user(self, dto: VerifyUserWithEmailGetCodeDTO):
        pass

    @override
    async def set_phone_code_verify_user(self, dto: VerifyUserWithPhoneSetCodeDTO):
        pass
