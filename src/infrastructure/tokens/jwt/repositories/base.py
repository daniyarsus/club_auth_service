from abc import ABC, abstractmethod
from datetime import datetime, timedelta

from jose import jwt, JWTError

from src.infrastructure.tokens.jwt.settings import (
    JWT_ACCESS_TOKEN_EXPIRE_SECONDS,
    JWT_REFRESH_TOKEN_EXPIRE_SECONDS,
    JWT_ALGORITHM,
    JWT_SECRET_KEY
)


class JWTAbstractRepository(ABC):
    @abstractmethod
    async def encode_token(self, token_type: str, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def decode_token(self, token: str):
        raise NotImplementedError


class JWTRepository(JWTAbstractRepository):
    async def encode_token(self, token_type: str, data: dict):
        try:
            encoded_data: dict = data.copy()

            if token_type == "access":
                expire: datetime = datetime.utcnow() + timedelta(seconds=int(JWT_ACCESS_TOKEN_EXPIRE_SECONDS))
            elif token_type == "refresh":
                expire: datetime = datetime.utcnow() + timedelta(seconds=int(JWT_REFRESH_TOKEN_EXPIRE_SECONDS))

            encoded_data.update(
                {
                    "exp": expire,
                    "type": token_type
                }
            )

            encoded_jwt = jwt.encode(
                encoded_data,
                key=JWT_SECRET_KEY,
                algorithm=JWT_ALGORITHM
            )

            return encoded_jwt

        except JWTError as e:
            raise e

    async def decode_token(self, token: str):
        try:
            decoded_jwt = jwt.decode(
                token,
                key=JWT_SECRET_KEY,
                algorithms=[JWT_ALGORITHM]
            )

            return decoded_jwt

        except JWTError as e:
            raise e
