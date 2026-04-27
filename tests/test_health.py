import pytest


@pytest.mark.asyncio
async def test_health_check(client):
    response = await client.get("/health")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_health_check_response_structure(client):
    response = await client.get("/health")
    data = response.json()

    assert "status" in data
    assert data["status"] == "ok"
    assert "app" in data
    assert "version" in data


@pytest.mark.asyncio
async def test_health_check_app_name(client):
    response = await client.get("/health")
    data = response.json()

    assert "Kata" in data["app"]
