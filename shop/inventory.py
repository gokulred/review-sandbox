STOCK = {"APPLE": 10, "PEAR": 0}


def get_item(sku: str) -> dict:
    return {"sku": sku, "qty": STOCK.get(sku, 0)}
