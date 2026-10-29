from shop.config import get_setting


def currency(settings: dict[str, str]) -> str:
    return get_setting(settings, "currency", "INR").upper()
