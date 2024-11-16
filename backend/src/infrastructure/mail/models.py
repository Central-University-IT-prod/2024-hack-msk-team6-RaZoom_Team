from pydantic import BaseModel, Field, EmailStr


class Mail(BaseModel):
    recipients: list[EmailStr]
    topic: str
    text: str
