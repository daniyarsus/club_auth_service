from injector import Injector, singleton

from src.domain.auth.interfaces import RegisterUserInterface
from src.domain.auth.services import RegisterUserService
from src.infrastructure.db.postgres_db.repositories import AbstractSQLUserRepository, SQLUserRepository
from src.infrastructure.db.redis_db.repositories import AbstractRedisAuthRepository, RedisAuthRepository
from src.infrastructure.tokens.jwt.repositories import AbstractAuthJWTRepository, AuthJWTRepository


def config(binder):
    binder.bind(interface=RegisterUserInterface, to=RegisterUserService, scope=singleton),
    binder.bind(interface=SQLUserRepository, to=SQLUserRepository, scope=singleton),
    binder.bind(interface=RedisAuthRepository, to=RedisAuthRepository, scope=singleton),
    binder.bind(interface=AbstractAuthJWTRepository, to=AbstractAuthJWTRepository, scope=singleton)
