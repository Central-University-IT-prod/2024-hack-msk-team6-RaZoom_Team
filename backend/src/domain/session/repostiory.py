from sqlmodel import select
from src.infrastructure.db import BaseRepository, User, Session


class SessionRepository(BaseRepository[Session]):

    async def get_by_id(self, id: str) -> Session:
        query = select(Session).where(Session.id == id)
        res = await self.session.exec(query)
        return res.first()

    async def insert(self, id: str, user: User) -> Session:
        return await self._insert(Session(
            id = id,
            user = user
        ))