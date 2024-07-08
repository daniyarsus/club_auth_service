from injector import singleton

from .base import JWTAbstractRepository, JWTRepository


@singleton
class AbstractAuthJWTRepository(JWTAbstractRepository):
    async def encode_token(self, token_type: str, data: dict):
        pass

    async def decode_token(self, token: str):
        pass


@singleton
class AuthJWTRepository(JWTRepository):
    pass
