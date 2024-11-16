from src.domain.client import ClientRepository
from src.infrastructure.mail import send_email, Mail


class MailService:

    def __init__(self) -> None:
        self.repo = ClientRepository()

    async def send_to(self, gender: str, age: str, status: str, title: str, text: str) -> None:
        emails = await self.repo.get_emails_by_filters(gender, age, status)
        for i in range(0, len(emails), 25):
            await send_email(Mail(recipients=emails[i:i+25], topic=title, text=text))