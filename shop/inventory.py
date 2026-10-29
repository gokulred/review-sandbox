STOCK = {"apple": 10, "pear": 0}


def get_item(sku: str) -> dict:
    return {"sku": sku, "qty": STOCK.get(sku, 0)}
