from shop.orders import can_order, order_price


def test_can_order_apple():
    assert can_order("apple", 2)


def test_order_price_with_coupon():
    assert order_price(100.0, 2, coupon_pct=10) == 180.0
