from abc import ABC
from sqlmodel import SQLModel

from .session import CTX_SESSION

class BaseRepository[T: SQLModel](ABC):

    def __init__(self) -> None:
        self.session = CTX_SESSION.get()

    async def get(self, **kwargs) -> T | None:
        raise NotImplementedError
    
    async def insert(self, **kwargs) -> T:
        raise NotImplementedError
    
    async def _insert(self, obj: T) -> T:
        self.session.add(obj)
        await self.session.flush()
        await self.session.refresh(obj)
        return obj
    
    async def delete(self, obj: T) -> None:
        await self.session.delete(obj)
        await self.session.flush()