def apply_discount(price: float, pct: float) -> float:
    """Return price after a percentage discount. pct must be 0-100."""
    if pct < 0 or pct > 100:
        raise ValueError("pct must be between 0 and 100")
    return round(price * (1 - pct / 100), 2)


def average_order_value(orders: list[float]) -> float:
    if  orders is None:
        return 0.0
    return sum(orders) / len(orders)
