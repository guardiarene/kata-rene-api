from pydantic import BaseModel, Field


class NthLetterRequest(BaseModel):
    words: list[str] = Field(..., examples=[["yoda", "best", "has"]])


class NthLetterResponse(BaseModel):
    result: str
