from fastapi import APIRouter, Depends

from src.application.session import SessionService
from src.application.user import UserService, get_auth
from src.domain.user import LoginUser, UserAuthenticated
from src.infrastructure.db import CTX_SESSION, Session, User

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("")
async def login(data: LoginUser) -> UserAuthenticated:
    """
    Аутентификация
    """

    user = await UserService().login(data.email, data.password)
    session = await SessionService().create(user)
    await CTX_SESSION.get().commit()
    return UserAuthenticated(session=session.id)

@router.delete("")
async def del_session(auth: tuple[Session, User] = Depends(get_auth)) -> bool:
    await SessionService().drop(auth[0])
    await CTX_SESSION.get().commit()
    return True