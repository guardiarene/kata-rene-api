import pytest


@pytest.mark.asyncio
async def test_create_entry_success(client):
    response = await client.post(
        "/dictionary/entry",
        json={"word": "Apple", "definition": "A fruit that grows on trees"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["word"] == "apple"
    assert data["definition"] == "A fruit that grows on trees"


@pytest.mark.asyncio
async def test_create_entry_duplicate_returns_409(client):
    payload = {"word": "Banana", "definition": "A yellow fruit"}
    await client.post("/dictionary/entry", json=payload)

    response = await client.post("/dictionary/entry", json=payload)
    assert response.status_code == 409


@pytest.mark.asyncio
async def test_lookup_existing_word(client):
    await client.post(
        "/dictionary/entry",
        json={"word": "Cherry", "definition": "A small red fruit"},
    )
    response = await client.get("/dictionary/entry/Cherry")
    assert response.status_code == 200
    assert response.json()["word"] == "cherry"


@pytest.mark.asyncio
async def test_lookup_case_insensitive(client):
    await client.post(
        "/dictionary/entry",
        json={"word": "mango", "definition": "A tropical fruit"},
    )
    response = await client.get("/dictionary/entry/MANGO")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_lookup_missing_word_returns_404(client):
    response = await client.get("/dictionary/entry/Banana")
    assert response.status_code == 404
    assert "Banana" in response.json()["detail"]
