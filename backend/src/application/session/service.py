import secrets

from src.domain.session import SessionRepository, User, Session


class SessionService:

    def __init__(self) -> None:
        self.repo = SessionRepository()

    async def create(self, user: User) -> Session:
        return await self.repo.insert(secrets.token_hex(32), user)
    
    async def drop(self, session: str) -> None:
        session = await SessionRepository().get_by_id(session)
        await self.repo.delete(session)