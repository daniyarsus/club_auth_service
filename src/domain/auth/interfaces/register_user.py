from abc import ABC, abstractmethod


class RegisterUserInterface(ABC):
    @abstractmethod
    def register_user(self, username: str, email: str, password: str):
        pass