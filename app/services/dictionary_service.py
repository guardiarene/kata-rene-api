from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.dictionary import Word


async def add_word(db: AsyncSession, word: str, definition: str) -> Word:
    existing = await db.execute(select(Word).where(Word.word == word.lower()))
    if existing.scalar_one_or_none():
        raise ValueError(f"Word '{word}' already exists in the dictionary.")

    new_word = Word(word=word.lower(), definition=definition)
    db.add(new_word)
    await db.commit()
    await db.refresh(new_word)
    return new_word


async def lookup_word(db: AsyncSession, word: str) -> Word | None:
    result = await db.execute(select(Word).where(Word.word == word.lower()))
    return result.scalar_one_or_none()
