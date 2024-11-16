from pydantic import BaseModel

from src.application.stage import BasicStage
from src.domain.stage import StageRepository
from src.enums import StageStatus
from src.infrastructure.db import Stage, User, Project
from src.infrastructure.exc import InvalidStage, BadRequest


class StageService:

    def __init__(self) -> None:
        self.repo = StageRepository()

    async def answer(self, payload: BaseModel, user: User, stage: Stage, project: Project) -> None:
        stage_cls = BasicStage.get(stage.stage)
        if stage.status != StageStatus.WORKING or stage_cls.executor != user.role:
            raise InvalidStage
        if not isinstance(payload, stage_cls.answer_model):
            raise BadRequest
        await stage_cls.answer(payload, stage, project)
        if stage.status == StageStatus.COMPLETED:
            for child in stage_cls.get_children():
                if all(map(
                    lambda c: project.get_stage(c).status == StageStatus.COMPLETED, child.depends_on,
                )):
                    await child.start(project.get_stage(child.type), project)