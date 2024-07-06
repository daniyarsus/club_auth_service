import redis
from redis import asyncio as aioredis

from src.config import settings


REDIS_URL = f"redis://{settings.REDIS_USER}:{settings.REDIS_PASS}@{settings.REDIS_HOST}:{settings.REDIS_PORT}"


sync_redis_conn = redis.from_url(REDIS_URL)

async_redis_conn = aioredis.from_url(REDIS_URL)
