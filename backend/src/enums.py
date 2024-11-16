from enum import Enum


class Role(Enum):
    PRODUCT = 0
    WRITER = 1
    HEAD_WRITER = 2
    ANALYST = 3

class StageType(Enum):
    WRITE_TEXT = 0
    APPROVE_TEXT = 1
    ANALYSIS = 2
    APPROVE = 3

class StageStatus(Enum):
    WAITING = 0
    WORKING = 1
    COMPLETED = 2