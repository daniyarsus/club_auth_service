from typing import NoReturn
from abc import ABC, abstractmethod


class LoginUserInterface(ABC):
    @abstractmethod
    async def authenticate_with_username(self, username: str, password: str) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def authenticate_with_email(self, email: str, password: str) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def authenticate_with_phone(self, phone: str, password: str) -> NoReturn:
        raise NotImplementedError
