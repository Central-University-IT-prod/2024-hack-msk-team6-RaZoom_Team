from src.application.stage import BasicStage
from src.domain.project import ProjectRepository, ProjectUserRepository, Role
from src.domain.stage import StageRepository
from src.domain.user import UserRepository
from src.infrastructure.db import Project, User
from src.infrastructure.exc import InvalidUser, RolesRestriction, Forbidden

class ProjectService:

    def __init__(self) -> None:
        self.repo = ProjectRepository()

    async def create(
        self,
        name: str,
        target_desc: str,
        goal: str,
        theme: str,
        product: User,
        users: list[int]
    ) -> Project:
        if product.role != Role.PRODUCT:
            raise Forbidden
        project = await self.repo.insert(name, target_desc, goal, theme)
        used_roles: list[Role] = [Role.PRODUCT]
        await ProjectUserRepository().insert(product, project)
        for user_id in users:
            user = await UserRepository().get_by_id(user_id)
            if not user:
                raise InvalidUser
            if user.role == Role.PRODUCT:
                raise RolesRestriction
            used_roles.append(user.role)
            await ProjectUserRepository().insert(user, project)
        if len(used_roles) != len(Role) or len(set(used_roles)) != len(used_roles):
            raise RolesRestriction
        await self.repo.session.refresh(project)
        for stage in BasicStage.get_all():
            await StageRepository().insert(await stage.created(project))
        return project