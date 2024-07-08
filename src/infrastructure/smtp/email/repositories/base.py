import smtplib
from abc import ABC, abstractmethod
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import NoReturn, override

from src.infrastructure.smtp.email.settings import (SMTP_API_KEY,
                                                    SMTP_DOMAIN_NAME,
                                                    SMTP_EMAIL_FROM, SMTP_PORT)


class AbstractSMTPEmailRepository(ABC):
    @abstractmethod
    async def send_message(self, message: str, to: str, subject: str) -> NoReturn:
        raise NotImplementedError


class SMTPEmailRepository(AbstractSMTPEmailRepository):
    @override
    async def send_message(self, message: str, to: str, subject: str):
        msg = MIMEMultipart()
        msg['From'] = SMTP_EMAIL_FROM
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(_text=message, _subtype='plain', _charset='utf-8'))

        server = smtplib.SMTP(SMTP_DOMAIN_NAME, SMTP_PORT)
        server.starttls()
        server.login(user=SMTP_EMAIL_FROM, password=SMTP_API_KEY)
        server.send_message(msg=msg)
        server.quit()
