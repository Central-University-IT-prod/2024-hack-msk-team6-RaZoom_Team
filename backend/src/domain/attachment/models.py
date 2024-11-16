from pydantic import BaseModel


class AttachmentDTO(BaseModel):
    filename: str
    url: str