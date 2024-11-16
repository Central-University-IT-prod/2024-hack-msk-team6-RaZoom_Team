from enum import Enum
from fastapi.responses import JSONResponse
from fastapi import Request


class ErrorCode(Enum):
    E404_NOTFOUND = 404 # 404
    E403_FORBIDDEN = 403 # 403
    E400_BADREQ = 400 # 400

    E1000_NOTAUTH = 1000 # 401
    E1001_EMAIL_ALREADY_REG = 1001 # 403
    E1002_PASSWORD_IS_INCORRECT = 1002 # 401
    E1003_INVALID_USER = 1003 # 404
    E1004_ROLES_RESTRICTION = 1004 # 403
    E1005_INVALID_STAGE = 1005 # 404

    E2000_INVALID_FILETYPE = 2000 # 400

class HTTPError(Exception):

    def __init__(
            self,
            http_code: int,
            error_code: ErrorCode,
            desc: str = None,
            additional: dict | None = None,
            headers: dict[str, str] | None = None
        ) -> None:
        self.http_code = http_code
        self.error_code = error_code
        self.desc = desc
        self.additional = additional or {}
        self.headers = headers or {}

    def __str__(self) -> str:
        return f"{self.http_code}_{self.error_code!r}: {self.desc}"

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(http_code={self.http_code!r}, error_code={self.error_code!r}, desc={self.desc!r})"
    
    @staticmethod
    async def handler(request: Request, exc: "HTTPError") -> JSONResponse:
        return JSONResponse(
            content={
                "code": exc.error_code.value,
                **({"desc": exc.desc} if exc.desc else {}),
                **exc.additional
            },
            status_code=exc.http_code,
            headers=exc.headers
        )

class NotFound(HTTPError):
    def __init__(self) -> None:
        super().__init__(404, ErrorCode.E404_NOTFOUND, "Not Found")

class Forbidden(HTTPError):
    def __init__(self) -> None:
        super().__init__(403, ErrorCode.E403_FORBIDDEN, "Forbidden")

class BadRequest(HTTPError):
    def __init__(self) -> None:
        super().__init__(403, ErrorCode.E400_BADREQ, "Bad request")