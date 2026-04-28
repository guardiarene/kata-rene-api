from fastapi import APIRouter

from app.schemas.shopping import ShoppingRequest, ShoppingResponse
from app.services.shopping_service import get_total

router = APIRouter(prefix="/shopping", tags=["shopping"])


@router.post("/total", response_model=ShoppingResponse)
async def calculate_total(payload: ShoppingRequest):
    total = get_total(payload.costs, payload.items, payload.tax)
    return ShoppingResponse(total=total)
