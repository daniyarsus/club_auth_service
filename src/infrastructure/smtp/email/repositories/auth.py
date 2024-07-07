from typing import NoReturn, override

from .base import AbstractSMTPEmailRepository, SMTPEmailRepository


class AbstractAuthSMTPEmailRepository(AbstractSMTPEmailRepository):
    @override
    async def send_message(self, recipient, subject, body) -> NoReturn:
        raise NotImplementedError


class AuthSMTPEmailRepository(SMTPEmailRepository):
    pass
