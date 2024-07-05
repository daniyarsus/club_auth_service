from typing import NoReturn
from abc import ABC, abstractmethod


class RegisterUserInterface(ABC):
    @abstractmethod
    async def register_user_with_email(self, email: str, username: str, password: str) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def get_email_code_verify_user(self, email: str) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def set_email_code_verify_user(self, email: str, code: str) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def register_user_with_phone(self, phone: str, username: str, password: str) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def get_phone_code_verify_user(self, phone: str) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def set_phone_code_verify_user(self, phone: str, code: str) -> NoReturn:
        raise NotImplementedError
