def cart_total(prices: list[float]) -> float:
    total = 0.0
    for i in range(len(prices)):
        total += prices[i]
    return round(total, 2)
