from abc import ABC, abstractmethod


class LoginUserInterface(ABC):
    @abstractmethod
    async def authenticate_with_username(self, username: str, password: str) -> None:
        raise NotImplementedError

    @abstractmethod
    async def authenticate_with_mail(self, email: str, password: str) -> None:
        raise NotImplementedError

    @abstractmethod
    async def authenticate_with_phone(self, phone: str, password: str) -> None:
        raise NotImplementedError
