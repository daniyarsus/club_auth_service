from typing import override

from injector import inject, singleton

from src.domain.auth.interfaces import RegisterUserInterface
from src.domain.auth.usecases import (

)
from src.infrastructure.db.postgres_db.repositories import (
    AbstractSQLUserRepository
)


@singleton
class RegisterUserService(RegisterUserInterface):
    @inject
    def __init__(
            self,
            user_repo: AbstractSQLUserRepository
    ) -> None:
        self.user_repo = user_repo

    @override
    async def register_user_with_email(self, email: str, username: str, password: str):
        pass

    @override
    async def get_email_code_verify_user(self, email: str):
        pass

    @override
    async def set_email_code_verify_user(self, email: str, code: str):
        pass

    @override
    async def register_user_with_phone(self, email: str, username: str, password: str):
        pass

    @override
    async def get_phone_code_verify_user(self, phone: str):
        pass

    @override
    async def set_phone_code_verify_user(self, phone: str, code: str):
        pass
