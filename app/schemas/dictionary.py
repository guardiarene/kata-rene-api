from pydantic import BaseModel, Field


class WordCreate(BaseModel):
    word: str = Field(..., min_length=1, max_length=100, examples=["Apple"])
    definition: str = Field(..., min_length=1, examples=["A fruit that grows on trees"])


class WordResponse(BaseModel):
    word: str
    definition: str

    model_config = {"from_attributes": True}
