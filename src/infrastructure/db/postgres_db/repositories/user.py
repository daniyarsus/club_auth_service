from typing import NoReturn, override

from .base import SQLAbstractRepository, SQLAlchemyRepository
from src.infrastructure.db.postgres_db.models import User


class AbstractUserRepository(SQLAbstractRepository):
    @override
    async def add_one(self, **data) -> NoReturn:
        raise NotImplementedError

    @override
    async def edit_one(self, data, **filters) -> NoReturn:
        raise NotImplementedError

    @override
    async def get_one(self, **filters) -> NoReturn:
        raise NotImplementedError

    @override
    async def get_several(self, from_, to) -> NoReturn:
        raise NotImplementedError

    @override
    async def get_all(self, **filters) -> NoReturn:
        raise NotImplementedError

    @override
    async def delete_one(self, **filters) -> NoReturn:
        raise NotImplementedError

    @override
    async def delete_several(self, ids) -> NoReturn:
        raise NotImplementedError

    @override
    async def delete_all(self, **filters) -> NoReturn:
        raise NotImplementedError


class UserRepository(SQLAlchemyRepository):
    model = User
