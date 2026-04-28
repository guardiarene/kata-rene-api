import pytest

from app.services.nth_letter_service import build_word


def test_build_word_basic():
    assert build_word(["yoda", "best", "has"]) == "yes"


def test_build_word_empty_list():
    assert build_word([]) == ""


def test_build_word_single_word():
    assert build_word(["hello"]) == "h"


@pytest.mark.asyncio
async def test_nth_letter_endpoint(client):
    response = await client.post(
        "/nth-letter/build",
        json={"words": ["yoda", "best", "has"]},
    )
    assert response.status_code == 200
    assert response.json()["result"] == "yes"


@pytest.mark.asyncio
async def test_nth_letter_empty_list(client):
    response = await client.post("/nth-letter/build", json={"words": []})
    assert response.status_code == 200
    assert response.json()["result"] == ""
