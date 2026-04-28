from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.config import settings
from app.db.session import Base, engine
from app.routers import dictionary, nth_letter, shopping


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="REST API exposing Python katas: Dictionary, Shopping and Nth Letter",
    lifespan=lifespan,
)

app.include_router(dictionary.router)
app.include_router(shopping.router)
app.include_router(nth_letter.router)


@app.get("/health", tags=["health"])
async def health_check():
    return {
        "status": "ok",
        "app": settings.app_name,
        "version": settings.app_version,
    }
