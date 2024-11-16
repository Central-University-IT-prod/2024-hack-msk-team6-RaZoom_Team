from sqlmodel import select
from sqlalchemy.orm.attributes import flag_modified

from src.infrastructure.db import BaseRepository
from src.infrastructure.db.tables import Stage


class StageRepository(BaseRepository[Stage]):

    async def get_by_id(self, id: int) -> Stage | None:
        query = select(Stage).where(Stage.id == id)
        res = await self.session.exec(query)
        return res.first()

    async def insert(self, stage: Stage) -> Stage:
        return await self._insert(stage)
    
    async def save_history(self, stage: Stage) -> None:
        stage.history_payload.append(stage.payload)
        flag_modified(stage, "history_payload")
        await self.session.flush()
        await self.session.refresh(stage)