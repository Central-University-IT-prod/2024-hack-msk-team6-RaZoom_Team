from sqlmodel import select
from src.infrastructure.db import BaseRepository, Attachment, User
from src.infrastructure.db.tables import Project


class AttachmentRepository(BaseRepository[Attachment]):

    async def get(self, id: str) -> Attachment | None:
        query = select(Attachment).where(Attachment.id == id)
        res = await self.session.exec(query)
        return res.first()
    
    async def insert(self, id: str, filename: str, project: Project) -> Attachment:
        return await self._insert(Attachment(
            id = id,
            filename = filename,
            project = project
        ))