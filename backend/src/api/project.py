import json
import math
from fastapi import APIRouter, Depends, File, HTTPException, Query, UploadFile

from src.application.attachment import AttachmentService
from src.application.project import ProjectService
from src.application.stage import get_stage, StageService, BasicStage
from src.application.user import get_user
from src.domain.project import RegisterProject, ProjectDTO, ProjectRepository, StageDTO, FetchProjects, FetchResult
from src.domain.project.models import ProjectInfo
from src.domain.stage import StageAnswerType
from src.infrastructure.db import CTX_SESSION, User, Stage, Project
from src.infrastructure.exc import Forbidden, NotFound


router = APIRouter(prefix="/projects", tags=["Projects"])


@router.get("/{project_id}")
async def get_project(project_id: int, user: User = Depends(get_user)) -> ProjectDTO:
    """
    Получение проекта
    """
    project = await ProjectRepository().get_by_id(project_id)
    if not project:
        raise NotFound
    if user not in project.users:
        raise Forbidden
    dto = ProjectDTO(
        **project.model_dump(),
        users = [i.model_dump() for i in project.users],
        stages = [i.model_dump() for i in project.stages],
        attachments = [i.model_dump() for i in project.attachments]
    )
    for stage in dto.stages:
        if not BasicStage.get(stage.stage).is_accesed(user):
            stage.payload = None
            stage.history_payload = None
            stage.comment = None
    return dto

@router.get("/fetch/")
async def fetch_projects(data: FetchProjects = Query(), user: User = Depends(get_user)) -> FetchResult:
    projects = await ProjectRepository().fetch(user, data.offset, data.limit, data.search)
    total = await ProjectRepository().count(user, data.search)
    return FetchResult(total = total, pages = math.ceil(total / data.limit), res = [
        ProjectInfo(**project.model_dump(), attachments=[i.model_dump() for i in project.attachments])
        for project in projects
    ])

@router.post("/{project_id}/{stage_id}")
async def answer_stage(
    payload: StageAnswerType,
    stage: tuple[Stage, Project] = Depends(get_stage),
    user: User = Depends(get_user), 
) -> StageDTO:
    """
    Отправка ответа по задаче
    """
    await StageService().answer(payload, user, stage[0], stage[1])
    await CTX_SESSION.get().commit()
    return stage[0]

@router.post("")
async def create_project(
    data: RegisterProject = Depends(),
    files: list[UploadFile] = File(default=[]),
    user: User = Depends(get_user)
) -> ProjectDTO:
    """
    Создание проекта
    """
    try:
        users = json.loads(data.users)
        if not isinstance(users, list):
            raise ValueError
    except (json.JSONDecodeError, TypeError, ValueError):
        raise HTTPException(400)
    project = await ProjectService().create(
        data.name, 
        data.target_desc, 
        data.goal, 
        data.theme, 
        user, 
        users
    )
    for file in files:
        await AttachmentService().upload(file, project)
    await CTX_SESSION.get().commit()
    return project