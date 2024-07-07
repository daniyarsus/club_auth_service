from typing import Any, override, NoReturn

from injector import singleton

from .base import RedisAbstractRepository, RedisRepository


@singleton
class AbstractRedisAuthRepository(RedisAbstractRepository):
    @override
    async def set_one(self, key: Any, value: Any, time_in_sec: int) -> NoReturn:
        raise NotImplementedError

    @override
    async def get_one(self, key: Any) -> NoReturn:
        raise NotImplementedError

    @override
    async def delete_one(self, key: Any) -> NoReturn:
        raise NotImplementedError

    @override
    async def delete_all(self, key: Any) -> NoReturn:
        raise NotImplementedError


class RedisAuthRepository(RedisRepository):
    pass
