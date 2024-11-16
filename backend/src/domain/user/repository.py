from sqlmodel import select, func

from src.enums import Role
from src.infrastructure.db import BaseRepository, User, Session
from src.infrastructure.utils import hash_password


class UserRepository(BaseRepository[User]):

    async def get_by_id(self, id: int) -> User | None:
        query = select(User).where(User.id == id)
        res = await self.session.exec(query)
        return res.first()

    async def get_by_auth(self, email: str, password: str) -> User | None:
        query = select(User).where(
            (User.email == email)
            & (User.password == hash_password(password))
        )
        res = await self.session.exec(query)
        return res.first()
    
    async def get_by_email(self, email: str) -> User | None:
        query = select(User).where(User.email == email)
        res = await self.session.exec(query)
        return res.first()

    async def get_by_session(self, session: str) -> User | None:
        query = select(User).join(Session, Session.id == session) \
            .where(Session.user_id == User.id) \
            # .options(selectinload(User.working_projects))
        res = await self.session.exec(query)
        return res.first()

    async def search(self, name: str, role: Role) -> list[User]:
        query = select(User).where((func.lower(User.name).like(f"%{name.lower()}%") | func.lower(User.email).like(f"%{name.lower()}%")) & (User.role == role)).limit(5)
        res = await self.session.exec(query)
        return res.all()

    async def insert(self, name: str, email: str, password_hash: str, role: Role) -> User:
        return await self._insert(User(
            email = email,
            name = name,
            password = password_hash,
            role = role
        ))