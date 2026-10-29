from shop.inventory import get_item
from shop.pricing import apply_discount


def can_order(sku: str, qty: int) -> bool:
    return get_item(sku)["qty"] >= qty


def order_price(price: float, qty: int, coupon_pct: float = 0) -> float:
    return apply_discount(price * qty, coupon_pct)
