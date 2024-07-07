from injector import singleton

from .base import JWTRepository, JWTAbstractRepository


@singleton
class AbstractAuthJWTRepository(JWTAbstractRepository):
    async def encode_token(self, token_type: str, data: dict):
        pass

    async def decode_token(self, token: str):
        pass


@singleton
class AuthJWTRepository(JWTRepository):
    pass
