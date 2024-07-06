from .base import JWTRepository, JWTAbstractRepository


class AbstractAuthJWTRepository(JWTAbstractRepository):
    async def encode_token(self, token_type: str, data: dict):
        pass

    async def decode_token(self, token: str):
        pass


class AuthJWTRepository(JWTRepository):
    pass