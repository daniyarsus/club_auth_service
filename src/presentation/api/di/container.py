from injector import singleton

from src.domain.auth.interfaces import (LoginUserInterface,
                                        RegisterUserInterface)
from src.domain.auth.services import LoginUserService, RegisterUserService
from src.infrastructure.db.postgres_db.repositories import (
    AbstractSQLUserRepository, SQLUserRepository)
from src.infrastructure.db.redis_db.repositories import (
    AbstractRedisAuthRepository, RedisAuthRepository)
from src.infrastructure.smtp.email.repositories import (
    AbstractAuthSMTPEmailRepository, AuthSMTPEmailRepository)
from src.infrastructure.tokens.jwt.repositories import (
    AbstractAuthJWTRepository, AuthJWTRepository)


def config(binder):
    binder.bind(interface=RegisterUserInterface, to=RegisterUserService, scope=singleton),
    binder.bind(interface=LoginUserInterface, to=LoginUserService, scope=singleton),
    binder.bind(interface=AbstractSQLUserRepository, to=SQLUserRepository, scope=singleton),
    binder.bind(interface=AbstractRedisAuthRepository, to=RedisAuthRepository, scope=singleton),
    binder.bind(interface=AbstractAuthJWTRepository, to=AuthJWTRepository, scope=singleton),
    binder.bind(interface=AbstractAuthSMTPEmailRepository, to=AuthSMTPEmailRepository, scope=singleton)
