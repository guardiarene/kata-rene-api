def get_total(costs: dict[str, float], items: list[str], tax: float) -> float:
    subtotal = sum(costs[item] for item in items if item in costs)
    return round(subtotal * (1 + tax), 2)
