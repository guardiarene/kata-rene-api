import pytest

from app.services.shopping_service import get_total


def test_get_total_basic():
    costs = {"socks": 5, "shoes": 60, "sweater": 30}
    assert get_total(costs, ["socks", "shoes"], 0.09) == 70.85


def test_get_total_ignores_missing_items():
    costs = {"socks": 5}
    assert get_total(costs, ["socks", "unknown_item"], 0.0) == 5.0


def test_get_total_empty_items():
    costs = {"socks": 5}
    assert get_total(costs, [], 0.09) == 0.0


def test_get_total_zero_tax():
    costs = {"socks": 5, "shoes": 60}
    assert get_total(costs, ["socks", "shoes"], 0.0) == 65.0


@pytest.mark.asyncio
async def test_shopping_endpoint(client):
    response = await client.post(
        "/shopping/total",
        json={
            "costs": {"socks": 5, "shoes": 60},
            "items": ["socks", "shoes"],
            "tax": 0.09,
        },
    )
    assert response.status_code == 200
    assert response.json()["total"] == 70.85


@pytest.mark.asyncio
async def test_shopping_endpoint_invalid_tax(client):
    response = await client.post(
        "/shopping/total",
        json={"costs": {}, "items": [], "tax": 1.5},  # tax > 1
    )
    assert response.status_code == 422
