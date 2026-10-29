def apply_discount(price: float, pct: float) -> float:
    """Return price after a  discount. pct is a fraction from 0 to 1."""
    if pct < 0 or pct > 1:
        raise ValueError("pct must be between 0 and 1")
    return round(price * (1 - pct), 2)


def average_order_value(orders: list[float]) -> float:
    if not orders:
        return 0.0
    return sum(orders) / len(orders)
