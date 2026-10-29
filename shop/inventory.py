STOCK = {"apple": 10, "pear": 0}


def get_item(sku: str) -> tuple[str,int]:
    return  sku,STOCK.get(sku, 0)
