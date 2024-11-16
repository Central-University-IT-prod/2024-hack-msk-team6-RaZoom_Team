from .core import HTTPError, ErrorCode


class InvalidUser(HTTPError):
    def __init__(self) -> None:
        super().__init__(404, ErrorCode.E1003_INVALID_USER, "Invalid user")

class AttachmentInvalidFiletype(HTTPError):
    def __init__(self) -> None:
        super().__init__(400, ErrorCode.E2000_INVALID_FILETYPE, "Invalid filtype (only: md, txt)")

class RolesRestriction(HTTPError):
    def __init__(self) -> None:
        super().__init__(403, ErrorCode.E1004_ROLES_RESTRICTION, "All roles should be used")