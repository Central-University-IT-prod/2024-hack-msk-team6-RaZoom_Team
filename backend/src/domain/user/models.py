from pydantic import BaseModel, EmailStr, Field

from src.domain.project.models import ProjectInfo
from src.enums import Role


class UserBase(BaseModel):
    name: str = Field(description="Имя пользователя", examples=["Андрей Иванов"])
    email: EmailStr = Field(max_length=254, description="Адресс электронной почты", examples=["example@mail.ru"])
    role: Role

# -----------------------------
#  RESPONSES
# -----------------------------

class BaseUserDTO(UserBase):
    id: int = Field(description="ID пользователя")

class UserDTO(BaseUserDTO):
    working_projects: list[ProjectInfo]

class UserAuthenticated(BaseModel):
    session: str = Field(description="Токен аутентификации",
                         examples=["e4578015a5f03a8c5915b7e759be1f26c6958d9f9827979bd24c872fd5d529be"])

class UserSearch(BaseModel):
    name: str = Field(description="Имя пользователя или email")
    role: Role

# -----------------------------
#  REQUESTS
# -----------------------------

class RegisterUser(UserBase):
    password: str = Field(description="Пароль")

class LoginUser(BaseModel):
    email: EmailStr = Field(max_length=254, description="Адресс электронной почты", examples=["example@mail.ru"])
    password: str = Field(description="Пароль")