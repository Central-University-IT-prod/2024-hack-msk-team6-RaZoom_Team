from .core import HTTPError, ErrorCode


class NotAuthorized(HTTPError):
    def __init__(self) -> None:
        super().__init__(401, ErrorCode.E1000_NOTAUTH, "Not authorized")

class EmailAlreadyRegistered(HTTPError):
    def __init__(self) -> None:
        super().__init__(403, ErrorCode.E1001_EMAIL_ALREADY_REG, "Email already registered")

class InvalidPassword(HTTPError):
    def __init__(self) -> None:
        super().__init__(401, ErrorCode.E1002_PASSWORD_IS_INCORRECT, "Password is incorrect")
