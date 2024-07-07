from typing import NoReturn, Optional, List, Any, TypeVar, Type, override
from abc import ABC, abstractmethod

from sqlalchemy import delete, update, insert
from sqlalchemy.future import select
from src.infrastructure.db.postgres_db.settings import async_session

T = TypeVar('T')


class SQLAbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, **data) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def edit_one(self, data, **filters) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, **filters) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def get_several(self, from_, to) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, **filters) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, **filters) -> NoReturn:
        raise NotImplementedError


class SQLAlchemyRepository(SQLAbstractRepository):
    model: Type[T] = None

    @override
    async def add_one(self, **data) -> Optional[Any]:
        async with async_session() as session:
            stmt = insert(self.model).values(**data)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one_or_none()

    @override
    async def edit_one(self, data: dict, **filters) -> Optional[Any]:
        async with async_session() as session:
            stmt = update(self.model).filter_by(**filters).values(**data).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one_or_none()

    @override
    async def get_one(self, **filters) -> Optional[Any]:
        async with async_session() as session:
            stmt = select(self.model).filter_by(**filters)
            res = await session.execute(stmt)
            entity = res.scalar_one_or_none()
            return entity

    @override
    async def get_several(self, from_: int = 0, to: int = 10, **filters) -> List[Any]:
        async with async_session() as session:
            stmt = select(self.model).filter_by(**filters).offset(from_).limit(to - from_)
            res = await session.execute(stmt)
            entities = res.scalars().all()
            return entities

    @override
    async def get_all(self, **filters) -> List[Any]:
        async with async_session() as session:
            stmt = select(self.model).filter_by(**filters)
            res = await session.execute(stmt)
            entities = res.scalars().all()
            return entities

    @override
    async def delete_one(self, **filters) -> int:
        async with async_session() as session:
            stmt = delete(self.model).filter_by(**filters)
            res = await session.execute(stmt)
            await session.commit()
            return res.rowcount

    @override
    async def delete_several(self, ids: List[int]) -> int:
        async with async_session() as session:
            stmt = delete(self.model).where(self.model.id.in_(ids))
            res = await session.execute(stmt)
            await session.commit()
            return res.rowcount
