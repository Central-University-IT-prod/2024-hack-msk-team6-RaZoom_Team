from typing import Literal, Union
from pydantic import BaseModel, field_validator

from src.enums import StageType


class StageAnswer[T: BaseModel](BaseModel):
    payload: T

class WriteTextAnswer(BaseModel):
    text: str

class ApproveTextAnswer(BaseModel):
    approved: bool
    comment: str = ""

class AnalysisAnswer(BaseModel):
    gender: Literal['male', 'female', 'all']
    age: Literal['child', 'teenager', 'adult', 'pensioner', 'all']
    status: Literal['new', 'main', 'sleeping', 'all']
    comment: str = ""

class StageProductAnswer(BaseModel):
    stage: StageType
    comment: str = ""

    @field_validator("stage")
    @classmethod
    def valid_stage(cls, stage: StageType) -> StageType:
        if stage not in [StageType.WRITE_TEXT, StageType.ANALYSIS]:
            raise ValueError("WRITE_TEXT and ANALYSIS only")
        return stage

class ApproveAnswer(BaseModel):
    not_approved: list[StageProductAnswer]

StageAnswerType = WriteTextAnswer | ApproveTextAnswer | AnalysisAnswer | ApproveAnswer