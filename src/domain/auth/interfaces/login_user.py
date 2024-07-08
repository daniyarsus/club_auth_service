from abc import ABC, abstractmethod
from typing import NoReturn


class LoginUserInterface(ABC):
    @abstractmethod
    async def authenticate_with_username(self, dto: dict) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def authenticate_with_email(self, dto: dict) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def authenticate_with_phone(self, dto: dict) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def get_refresh_token(self, token: str) -> NoReturn:
        raise NotImplementedError
