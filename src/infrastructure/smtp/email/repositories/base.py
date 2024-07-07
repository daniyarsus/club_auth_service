from abc import ABC, abstractmethod
from typing import NoReturn, override

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from src.infrastructure.smtp.email.settings import (
    SMTP_DOMAIN_NAME,
    SMTP_PORT,
    SMTP_API_KEY,
    SMTP_EMAIL_FROM
)


class AbstractSMTPEmailRepository(ABC):
    @abstractmethod
    async def send_message(self, message: str, to: str, subject: str):
        raise NotImplementedError


class SMTPEmailRepository(AbstractSMTPEmailRepository):
    @override
    async def send_message(self, message: str, to: str, subject: str):
        msg = MIMEMultipart()
        msg['From'] = SMTP_EMAIL_FROM
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain', 'utf-8'))

        server = smtplib.SMTP(SMTP_DOMAIN_NAME, SMTP_PORT)
        server.starttls()
        server.login(SMTP_EMAIL_FROM, SMTP_API_KEY)
        server.send_message(msg)
        server.quit()
