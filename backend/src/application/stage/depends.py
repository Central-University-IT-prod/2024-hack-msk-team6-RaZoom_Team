from fastapi import Depends

from src.application.user import get_user
from src.domain.project import ProjectRepository
from src.domain.stage import StageRepository
from src.infrastructure.db import Stage, User, Project
from src.infrastructure.exc import Forbidden, NotFound


async def get_stage(stage_id: int, project_id: int, user: User = Depends(get_user)) -> tuple[Stage, Project]:
    project = await ProjectRepository().get_by_id(project_id)
    if not project:
        raise NotFound
    stage = await StageRepository().get_by_id(stage_id)
    if not stage:
        raise NotFound
    if stage.project_id != project.id or user not in project.users:
        raise Forbidden
    return stage, project