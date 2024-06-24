from abc import ABC, abstractmethod

from sqlalchemy import select, delete, update, insert
from sqlalchemy.future import select as async_select
from src.infrastructure.db.postgres_db.settings import async_session


class SQLAbstractRepository(ABC):
    model = None

    @abstractmethod
    async def add_one(self, **data):
        raise NotImplementedError

    @abstractmethod
    async def edit_one(self, data, **filters):
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, **filters):
        raise NotImplementedError

    @abstractmethod
    async def get_several(self, from_, to):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, **filters):
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, **filters):
        raise NotImplementedError

    @abstractmethod
    async def delete_several(self, ids):
        raise NotImplementedError


class SQLAlchemyRepository(SQLAbstractRepository):
    model = None

    async def add_one(self, **data):
        async with async_session() as session:
            stmt = insert(self.model).values(**data)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one_or_none()

    async def edit_one(self, data, **filters):
        async with async_session() as session:
            stmt = update(self.model).filter_by(**filters).values(**data).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one_or_none()

    async def get_one(self, **filters):
        async with async_session() as session:
            stmt = select(self.model).filter_by(**filters)
            res = await session.execute(stmt)
            entity = res.scalar_one_or_none()
            return entity

    async def get_several(self, from_: int = 0, to: int = 10, **filters):
        async with async_session() as session:
            stmt = select(self.model).filter_by(**filters).offset(from_).limit(to - from_)
            res = await session.execute(stmt)
            entities = res.scalars().all()
            return entities

    async def get_all(self, **filters):
        async with async_session() as session:
            stmt = select(self.model).filter_by(**filters)
            res = await session.execute(stmt)
            entities = res.scalars().all()
            return entities

    async def delete_one(self, **filters):
        async with async_session() as session:
            stmt = delete(self.model).filter_by(**filters)
            res = await session.execute(stmt)
            await session.commit()
            return res.rowcount

    async def delete_several(self, **filters):
        async with async_session() as session:
            stmt = delete(self.model).where(self.model.id.in_(**filters))
            res = await session.execute(stmt)
            await session.commit()
            return res.rowcount
