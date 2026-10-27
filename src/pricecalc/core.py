def apply_discount(price: float, percent: float) -> float:
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price * (1 - percent / 100), 2)


def add_tax(price: float, rate: float) -> float:
    return round(price * (1 + rate), 2)


def total(prices: list[float], discount: float = 0.0, tax_rate: float = 0.0) -> float:
    subtotal = sum(prices)
    return add_tax(apply_discount(subtotal, discount), tax_rate)
