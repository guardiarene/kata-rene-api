from fastapi import APIRouter

from app.schemas.nth_letter import NthLetterRequest, NthLetterResponse
from app.services.nth_letter_service import build_word

router = APIRouter(prefix="/nth-letter", tags=["nth-letter"])


@router.post("/build", response_model=NthLetterResponse)
async def build_nth_letter_word(payload: NthLetterRequest):
    result = build_word(payload.words)
    return NthLetterResponse(result=result)
