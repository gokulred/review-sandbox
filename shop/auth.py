from shop.users import find_user


def login(conn, email: str) -> bool:
    return find_user(conn, email) is not None
