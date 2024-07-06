from injector import inject
from fastapi import HTTPException, status

from src.domain.auth.dto import LoginUserWithUsernameDTO, LoginUserWithEmailDTO, LoginUserWithPhoneDTO
from src.domain.auth.exceptions import *
from src.infrastructure.db.postgres_db.repositories import AbstractSQLUserRepository
from src.infrastructure.db.redis_db.repositories import AbstractRedisAuthRepository
from src.infrastructure.smtp.email.repositories import *
from src.infrastructure.smtp.sms.repositories import *
from src.infrastructure.tokens.jwt.repositories import AbstractAuthJWTRepository