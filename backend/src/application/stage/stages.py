import asyncio
from pydantic import BaseModel
from src.application.mail.service import MailService
from src.domain.stage import WriteTextAnswer, ApproveTextAnswer, AnalysisAnswer, ApproveAnswer
from src.domain.stage.repository import StageRepository
from src.enums import Role, StageStatus, StageType
from src.infrastructure.db import Project, Stage, User
from src.infrastructure.db.session import CTX_SESSION
from src.infrastructure.mail.mail import send_email
from src.infrastructure.mail.models import Mail


class BasicStage:
    _all_stages: list["BasicStage"] = []

    type: StageType
    executor: Role
    answer_model: BaseModel
    additional_access: list[Role] = []
    depends_on: list[StageType] = []

    @staticmethod
    def get_all() -> list["BasicStage"]:
        return BasicStage._all_stages

    @staticmethod
    def get(type: StageType) -> "BasicStage":
        return next(filter(lambda s: s.type == type, BasicStage._all_stages))

    @classmethod
    def get_children(cls) -> list["BasicStage"]:
        return list(filter(lambda s: cls.type in s.depends_on, BasicStage.get_all()))

    @classmethod
    async def created(cls, project: Project) -> Stage:
        stage = Stage(
            project = project,
            stage = cls.type,
            status = StageStatus.WAITING,
            payload = {},
            history_payload = []
        )
        if not cls.depends_on:
            await cls.start(stage, project)
        return stage
    
    @classmethod
    async def start(cls, stage: Stage, project: Project) -> None:
        stage.status = StageStatus.WORKING
        executor = next(filter(lambda u: u.role == cls.executor, project.users))
        await cls.send_notify(executor, project)
    
    @classmethod
    def is_accesed(cls, user: User) -> bool:
        return user.role in cls.additional_access + [cls.executor, Role.PRODUCT]

    @staticmethod
    async def answer(payload: BaseModel, stage: Stage, project: Project) -> None:
        stage.payload = payload.model_dump()
        stage.status = StageStatus.COMPLETED

    @classmethod
    async def send_notify(cls, user: User, project: Project) -> None:
        asyncio.ensure_future(send_email(Mail(
            recipients = [user.email],
            topic = "Ваша задача перешла в активный статус",
            text = f"**{user.name}**, вам была добавлена новая задача в проекте **\"{project.name}\"**."
        )))

    @staticmethod
    def _stage[T: type[BasicStage]](cls: T) -> T:
        BasicStage._all_stages.append(cls)
        return cls

@BasicStage._stage
class WriterStage(BasicStage):
    type = StageType.WRITE_TEXT
    executor = Role.WRITER
    additional_access = [Role.HEAD_WRITER]
    answer_model = WriteTextAnswer
    depends_on = []

@BasicStage._stage
class HeadWriterStage(BasicStage):
    type = StageType.APPROVE_TEXT
    executor = Role.HEAD_WRITER
    answer_model = ApproveTextAnswer
    depends_on = [StageType.WRITE_TEXT]

    @staticmethod
    async def answer(payload: ApproveTextAnswer, stage: Stage, project: Project) -> None:
        stage.payload = payload.model_dump()
        text_stage = project.get_stage(StageType.WRITE_TEXT)
        if payload.approved:
            stage.status = StageStatus.COMPLETED
            text_stage.comment = payload.comment
        else:
            stage.status = StageStatus.WAITING
            text_stage.status = StageStatus.WORKING
            text_stage.history_payload.append(text_stage.payload)
            text_stage.comment = payload.comment

@BasicStage._stage
class AnalysisStage(BasicStage):
    type = StageType.ANALYSIS
    executor = Role.ANALYST
    answer_model = AnalysisAnswer
    depends_on = []

@BasicStage._stage
class ApproveStage(BasicStage):
    type = StageType.APPROVE
    executor = Role.PRODUCT
    answer_model = ApproveAnswer
    depends_on = [StageType.ANALYSIS, StageType.APPROVE_TEXT]

    @staticmethod
    async def answer(payload: ApproveAnswer, stage: Stage, project: Project) -> None:
        if not payload.not_approved:
            stage.status = StageStatus.COMPLETED
            project.is_archive = True
            text = project.get_stage(StageType.WRITE_TEXT)
            analysis = project.get_stage(StageType.ANALYSIS)
            asyncio.ensure_future(MailService().send_to(
                analysis.payload['gender'],
                analysis.payload['age'],
                analysis.payload['status'],
                project.theme,
                text.payload['text']
            ))
        else:
            stage.status = StageStatus.WAITING
            for st in payload.not_approved:
                obj = project.get_stage(st.stage)
                await BasicStage.get(st.stage).start(obj, project=project)
                # obj.history_payload.append(obj.payload)
                await StageRepository().save_history(obj)
                obj.comment = st.comment
                for child in BasicStage.get(st.stage).get_children():
                    child = project.get_stage(type=child.type)
                    child.status = StageStatus.WAITING
                    await StageRepository().save_history(child)