from pydantic import BaseModel, Field, field_validator

from src.domain.attachment import AttachmentDTO
from src.enums import Role, StageType, StageStatus
from src.infrastructure.db import Attachment


# -----------------------------
#  RESPONSES
# -----------------------------

class ProjectUserDTO(BaseModel):
    id: int
    name: str = Field(description="Имя пользователя", examples=["Андрей Иванов"])
    role: Role

class StageDTO(BaseModel):
    id: int
    stage: StageType
    status: StageStatus
    payload: dict | None
    history_payload: list[dict] | None
    comment: str | None

class ProjectInfo(BaseModel):
    id: int
    name: str
    theme: str
    target_desc: str
    goal: str
    is_archive: bool
    attachments: list[AttachmentDTO]

    # @field_validator("attachments", mode="before")
    # @classmethod
    # def valid_attachments(cls, atchs: list[Attachment] | list[str]):
    #     if atchs and isinstance(atchs[0], Attachment):
    #         return [atch.url for atch in atchs]
    #     return atchs

class ProjectDTO(ProjectInfo):
    users: list[ProjectUserDTO]
    stages: list[StageDTO]


# -----------------------------
#  REQUESTS
# -----------------------------

class FetchProjects(BaseModel):
    search: str | None = None
    offset: int = Field(ge=0, default=0)
    limit: int = Field(le=25, default=25)

class RegisterProject(BaseModel):
    name: str = Field(min_length=3, max_length=128, description="Название проекта")
    theme: str = Field(min_length=3, max_length=128, description="Тема проекта")
    target_desc: str = Field(min_length=3, max_length=256, description="Описание ЦА")
    goal: str = Field(min_length=3, max_length=256, description="Цель проекта")
    users: str

class FetchResult(BaseModel):
    total: int
    pages: int
    res: list[ProjectInfo]