from urllib.parse import quote
from fastapi import APIRouter, Response

from src.application.attachment import AttachmentService
from src.infrastructure.exc import NotFound


router = APIRouter(prefix="/attachments", tags=["Attachments"])

@router.get("/{id}")
async def get_attachment(id: str) -> bytes:
    file, filename = await AttachmentService().download_file(id)
    return Response(
        content = file,
        media_type = "application/octet-stream",
        headers = {'Content-Disposition': f'attachment; filename="{quote(filename)}"'}
    )