from typing import override

from injector import inject, singleton

from src.domain.auth.dto import (RegisterUserWithEmailDTO,
                                 RegisterUserWithPhoneDTO,
                                 VerifyUserWithEmailGetCodeDTO,
                                 VerifyUserWithEmailSetCodeDTO,
                                 VerifyUserWithPhoneGetCodeDTO,
                                 VerifyUserWithPhoneSetCodeDTO)
from src.domain.auth.interfaces import RegisterUserInterface
from src.domain.auth.usecases import (RegisterUserWithEmailUseCase,
                                      VerifyUserWithEmailGetCodeUseCase,
                                      VerifyUserWithEmailSetCodeUseCase)
from src.infrastructure.db.postgres_db.repositories import \
    AbstractSQLUserRepository
from src.infrastructure.db.redis_db.repositories import \
    AbstractRedisAuthRepository
from src.infrastructure.smtp.email.repositories import \
    AbstractAuthSMTPEmailRepository


@singleton
class RegisterUserService(RegisterUserInterface):
    @inject
    def __init__(
            self,
            sql_user_repository: AbstractSQLUserRepository,
            redis_auth_repository: AbstractRedisAuthRepository,
            auth_smtp_email_repository: AbstractAuthSMTPEmailRepository
    ) -> None:
        self.sql_user_repository = sql_user_repository
        self.redis_auth_repository = redis_auth_repository
        self.auth_smtp_email_repository = auth_smtp_email_repository

    @override
    async def register_user_with_email(self, dto: RegisterUserWithEmailDTO):
        use_case: RegisterUserWithEmailUseCase = RegisterUserWithEmailUseCase(
            sql_user_repository=self.sql_user_repository
        )
        return await use_case(
            dto=dto
        )

    @override
    async def get_email_code_verify_user(self, dto: VerifyUserWithEmailGetCodeDTO):
        use_case: RegisterUserWithEmailUseCase = VerifyUserWithEmailGetCodeUseCase(
            sql_user_repository=self.sql_user_repository,
            redis_auth_repository=self.redis_auth_repository,
            auth_smtp_email_repository=self.auth_smtp_email_repository
        )
        return await use_case(
            dto=dto
        )

    @override
    async def set_email_code_verify_user(self, dto: VerifyUserWithEmailSetCodeDTO):
        use_case: RegisterUserWithEmailUseCase = VerifyUserWithEmailSetCodeUseCase(
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
    async def get_phone_code_verify_user(self, dto: VerifyUserWithPhoneGetCodeDTO):
        pass

    @override
    async def set_phone_code_verify_user(self, dto: VerifyUserWithPhoneSetCodeDTO):
        pass
