from fastapi import Depends, Security
from fastapi.security import APIKeyHeader

from src.domain.user import UserRepository
from src.infrastructure.db import User, Session
from src.infrastructure.exc import NotAuthorized


api_key = APIKeyHeader(name = "Authorization", auto_error = False)

async def get_auth(session: str | None = Security(api_key)) -> tuple[str, User]:
    if not session:
        raise NotAuthorized
    
    user = await UserRepository().get_by_session(session)
    if not user:
        raise NotAuthorized
    
    return session, user

async def get_user(auth: tuple[str, User] = Depends(get_auth)) -> User:
    return auth[1]