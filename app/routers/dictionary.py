from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.dictionary import WordCreate, WordResponse
from app.services.dictionary_service import add_word, lookup_word

router = APIRouter(prefix="/dictionary", tags=["dictionary"])


@router.post(
    "/entry",
    response_model=WordResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_entry(payload: WordCreate, db: AsyncSession = Depends(get_db)):
    try:
        word = await add_word(db, payload.word, payload.definition)
        return word
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.get("/entry/{word}", response_model=WordResponse)
async def get_entry(word: str, db: AsyncSession = Depends(get_db)):
    result = await lookup_word(db, word)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Can't find entry for {word}",
        )
    return result
