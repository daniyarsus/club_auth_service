from typing import Any, NoReturn, override
from abc import ABC, abstractmethod

from src.infrastructure.db.redis_db.settings import async_redis_conn


class RedisAbstractRepository(ABC):
    @abstractmethod
    async def set_one(self, key: Any, value: Any, time_in_sec: int) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, key: Any) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, key: Any) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def delete_all(self, key: Any) -> NoReturn:
        raise NotImplementedError


class RedisRepository(RedisAbstractRepository):
    @override
    async def set_one(self, key: Any, value: Any, time_in_sec: int):
        res = await async_redis_conn.set(name=f"{key}", value=value, ex=time_in_sec)
        return res

    @override
    async def get_one(self, key: Any):
        res = await async_redis_conn.get(name=f"{key}")
        return res

    @override
    async def delete_one(self, key: Any):
        res = await async_redis_conn.delete(f"{key}")
        return res

    @override
    async def delete_all(self, key: Any):
        all_keys = await async_redis_conn.keys('*')
        for key in all_keys:
            if key.startswith(b"" + str(key).encode("utf-8")):
                await async_redis_conn.delete(key)
