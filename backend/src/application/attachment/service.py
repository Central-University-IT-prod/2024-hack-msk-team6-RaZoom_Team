import os
import uuid
import aiofiles
from fastapi import UploadFile

from src.domain.attachment import AttachmentRepository
from src.infrastructure.db import Attachment, Project
from src.infrastructure.exc import NotFound, AttachmentInvalidFiletype


class AttachmentService:

    def __init__(self) -> None:
        self.repo = AttachmentRepository()

    async def save_file(self, file: bytes, id: str) -> None:
        if not os.path.exists("data"):
            os.mkdir("data")
        async with aiofiles.open(f"data/{id}", "wb") as f:
            await f.write(file)
        
    async def delete_file(self, attachment: Attachment) -> None:
        try:
            os.remove(f"data/{attachment.id}")
        except OSError:
            pass

    async def upload(self, file: UploadFile, project: Project) -> Attachment:
        # if file.filename.split(".")[-1] not in ["md", "txt"]:
        #     raise AttachmentInvalidFiletype
        atch = await self.repo.insert(id = str(uuid.uuid4()), filename = file.filename, project = project)
        await self.save_file(file.file.read(), atch.id)
        return atch
    
    async def download_file(self, id: str) -> tuple[bytes, str]:
        atch = await self.repo.get(id)
        if not atch: raise NotFound

        async with aiofiles.open(f"data/{atch.id}", "rb") as f:
            return await f.read(), atch.filename

    async def delete(self, attachment: Attachment) -> None:
        await self.delete_file(attachment)
        await self.repo.delete(attachment)