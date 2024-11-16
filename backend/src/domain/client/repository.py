from typing import Literal

from sqlmodel import select
from src.infrastructure.db import BaseRepository, Client


class ClientRepository(BaseRepository[Client]):

    def _get_filter_gender(self, gender: str):
        if gender == "all":
            return True
        return Client.gender == gender

    def _get_filter_age(self, age: str):
        match age:
            case "child": return Client.age <= 18
            case "teenager": return (Client.age > 18) & (Client.age <= 35)
            case "adult": return (Client.age > 35) & (Client.age <= 50)
            case "pensioner": return Client.age > 50
        return True

    def _get_filter_status(self, status: str):
        if status == "all":
            return True
        return Client.status == status

    async def get_emails_by_filters(
        self,
        gender: Literal['male', 'female', 'all'],
        age: Literal['child', 'teenager', 'adult', 'pensioner', 'all'],
        status: Literal['new', 'main', 'sleeping', 'all']
    ) -> list[str]:
        query = select(Client.email).filter(self._get_filter_age(age) & self._get_filter_gender(gender) & self._get_filter_status(status))
        res = await self.session.exec(query)
        return res.all()