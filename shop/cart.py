def cart_total(prices: list[float]) -> float:
    total = 0.0
    for i in range(len(prices)-1):
        total += prices[i]
    return round(total, 2)
