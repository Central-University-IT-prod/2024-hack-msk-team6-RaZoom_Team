from fastapi import APIRouter, Depends

from src.application.session import SessionService
from src.application.user import get_user, UserService
from src.domain.project import ProjectInfo, ProjectRepository
from src.domain.user import UserDTO, RegisterUser, UserAuthenticated, BaseUserDTO, UserSearch, UserRepository
from src.infrastructure.db import User, CTX_SESSION


router = APIRouter(prefix="/users", tags=["Users"])

@router.get("")
async def get_user_info(user: User = Depends(get_user)) -> UserDTO:
    """
    Получение информации о пользователе
    """
    projects = await ProjectRepository().get_working_user(user)
    return UserDTO(
        **user.model_dump(),
        working_projects = [ProjectInfo(**project.model_dump(),
        attachments=[i.model_dump() for i in project.attachments]) for project in projects]
    )

@router.post("")
async def register(data: RegisterUser) -> UserAuthenticated:
    """
    Получение информации о пользователе
    """
    user = await UserService().register(data.email, data.name, data.password, data.role)
    session = await SessionService().create(user)
    await CTX_SESSION.get().commit()
    return UserAuthenticated(session = session.id)

@router.post("/search")
async def search(data: UserSearch, user: User = Depends(get_user)) -> list[BaseUserDTO]:
    """
    Поиск пользователей
    """
    return await UserRepository().search(data.name, data.role)