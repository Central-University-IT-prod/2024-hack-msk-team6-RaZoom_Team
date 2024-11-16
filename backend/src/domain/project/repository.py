from sqlmodel import desc, select, func

from src.infrastructure.db import BaseRepository, Project, ProjectUser, User


class ProjectRepository(BaseRepository[Project]):

    async def get_by_id(self, id: int) -> Project | None:
        query = select(Project).where(Project.id == id)
        res = await self.session.exec(query)
        return res.first()
    
    async def get_working_user(self, user: User) -> list[Project]:
        query = select(Project).join(ProjectUser).where((ProjectUser.user_id == user.id) & (Project.is_archive == False))
        res = await self.session.exec(query)
        return res.all()

    async def fetch(self, user: User, offset: int, limit: int, search: str | None) -> list[Project]:
        query = select(Project) \
            .offset(offset) \
            .limit(limit) \
            .order_by(desc(Project.id)) \
            .join(ProjectUser, ProjectUser.project_id == Project.id) \
            .where(ProjectUser.user_id == user.id)
        if search:
            query = query.where(func.lower(Project.name).like(f"%{search.lower()}%"))
        res = await self.session.exec(query)
        return res.all()
    
    async def count(self, user: User, search: str) -> int:
        query = select(func.count()) \
            .select_from(Project) \
            .join(ProjectUser, ProjectUser.project_id == Project.id) \
            .where(ProjectUser.user_id == user.id)
        if search:
            query = query.where(func.lower(Project.name).like(f"%{search.lower()}%"))
        res = await self.session.exec(query)
        return res.first()

    async def insert(
            self,
            name: str,
            target_desc: str,
            goal: str,
            theme: str
        ) -> Project:
        return await self._insert(Project(
            name = name,
            target_desc = target_desc,
            goal = goal,
            theme = theme,
        ))
    
class ProjectUserRepository(BaseRepository[ProjectUser]):

    # async def get_by_id(self, id: int) -> ProjectUser | None:
    #     query = select(ProjectUser).where(ProjectUser.user_id == id)
    #     res = await self.session.exec(query)
    #     return res.first()
    
    async def insert(self, user: User, project: Project) -> ProjectUser:
        return await self._insert(ProjectUser(
            user_id = user.id,
            project_id = project.id
        ))