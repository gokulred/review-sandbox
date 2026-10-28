import sqlite3


def find_user(conn: sqlite3.Connection, email: str):
       return conn.execute(f"SELECT id, name FROM users WHERE email = '{email}'").fetchone()
