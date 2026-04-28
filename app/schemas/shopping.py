from pydantic import BaseModel, Field


class ShoppingRequest(BaseModel):
    costs: dict[str, float] = Field(
        ..., examples=[{"socks": 5, "shoes": 60, "sweater": 30}]
    )
    items: list[str] = Field(..., examples=[["socks", "shoes"]])
    tax: float = Field(..., ge=0, le=1, examples=[0.09])


class ShoppingResponse(BaseModel):
    total: float
