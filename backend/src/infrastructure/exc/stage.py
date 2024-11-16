from .core import HTTPError, ErrorCode


class InvalidStage(HTTPError):
    def __init__(self) -> None:
        super().__init__(404, ErrorCode.E1005_INVALID_STAGE, "Invalid stage")