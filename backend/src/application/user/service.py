from src.domain.user import UserRepository
from src.enums import Role
from src.infrastructure.db import User
from src.infrastructure.utils import hash_password
from src.infrastructure.exc import EmailAlreadyRegistered, InvalidPassword


class UserService:

    def __init__(self) -> None:
        self.repo = UserRepository()

    async def register(self, email: str, name: str, password: str, role: Role) -> User:
        if await self.repo.get_by_email(email):
            raise EmailAlreadyRegistered
        return await self.repo.insert(name, email, hash_password(password), role = role)

    async def login(self, email: str, password: str) -> User:
        user = await self.repo.get_by_auth(email=email, password=password)
        if not user:
            raise InvalidPassword
        return user