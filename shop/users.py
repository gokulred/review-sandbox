import sqlite3


def get_user_by_email(conn: sqlite3.Connection, email: str):
    return conn.execute("SELECT id, name FROM users WHERE email = ?", (email,)).fetchone()
