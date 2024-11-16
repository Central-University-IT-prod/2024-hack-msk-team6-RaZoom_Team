from typing import Literal
from pydantic import computed_field
from sqlalchemy import ARRAY, JSON, String, text
from sqlmodel import Field, Relationship, SQLModel

from src.config import API_URL
from src.enums import Role, StageType, StageStatus


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int = Field(primary_key=True)
    email: str = Field(unique=True, index=True)
    name: str
    password: str
    role: Role

    # working_projects: list["Project"] = Relationship(
    #     sa_relationship_kwargs={
    #         "primaryjoin": "and_(ProjectUser.user_id == User.id, Project.is_archive == False)",
    #         "secondary": "project_users",
    #         "viewonly": True
    #     }
    # )

class Session(SQLModel, table=True):
    __tablename__ = "sessions"

    id: str = Field(primary_key=True)
    user_id: int = Field(foreign_key="users.id", ondelete="CASCADE")

    user: User = Relationship()

class Project(SQLModel, table=True):
    __tablename__ = "projects"

    id: int = Field(primary_key=True)
    name: str
    theme: str
    target_desc: str
    goal: str
    is_archive: bool = Field(sa_column_kwargs={"server_default": text("false")})

    users: list["User"] = Relationship(sa_relationship_kwargs={
        "secondary": "project_users",
        "lazy": "selectin"
    })
    stages: list["Stage"] = Relationship(back_populates="project", sa_relationship_kwargs={"lazy": "selectin"})
    attachments: list["Attachment"] = Relationship(back_populates="project", sa_relationship_kwargs={"lazy": "selectin"})

    def get_stage(self, type: StageType) -> "Stage":
        return next(filter(lambda s: s.stage == type, self.stages), None)

class ProjectUser(SQLModel, table=True):
    __tablename__ = "project_users"

    id: int = Field(primary_key=True)
    project_id: int = Field(foreign_key="projects.id", index=True, ondelete="CASCADE")
    user_id: int = Field(foreign_key="users.id", ondelete="CASCADE")

class Stage(SQLModel, table=True):
    __tablename__ = "stages"

    id: int = Field(primary_key=True)
    project_id: int = Field(foreign_key="projects.id", ondelete="CASCADE")
    stage: StageType
    status: StageStatus
    payload: dict = Field(sa_type=JSON)
    history_payload: list[dict] = Field(sa_type=ARRAY(JSON))
    comment: str | None

    project: Project = Relationship(back_populates="stages")

class Attachment(SQLModel, table=True):
    __tablename__ = "attachments"

    id: str = Field(primary_key=True)
    filename: str
    project_id: int = Field(foreign_key="projects.id", ondelete="CASCADE")

    project: Project = Relationship(back_populates="attachments")

    @computed_field
    @property
    def url(self) -> str:
        return API_URL + "/attachments/" + self.id

class Client(SQLModel, table=True):
    __tablename__ = "clients"

    id: int = Field(primary_key=True)
    email: str
    age: int
    gender: Literal['male', 'female'] = Field(sa_type=String)
    status: Literal['new', 'main', 'sleeping'] = Field(sa_type=String)