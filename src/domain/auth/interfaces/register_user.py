from abc import ABC, abstractmethod
from typing import NoReturn


class RegisterUserInterface(ABC):
    @abstractmethod
    async def register_user_with_email(self, dto: dict) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def get_email_code_verify_user(self, dto: dict) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def set_email_code_verify_user(self, dto: dict) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def register_user_with_phone(self, dto: dict) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def get_phone_code_verify_user(self, dto: dict) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def set_phone_code_verify_user(self, dto: dict) -> NoReturn:
        raise NotImplementedError
