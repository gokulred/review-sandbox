import os

import httpx

PAYMENTS_URL = "https://api.example-payments.com/v1/charges"


def charge(amount_cents: int, token: str) -> dict:
    api_key = os.environ["PAYMENTS_API_KEY"]
    r = httpx.post(PAYMENTS_URL, json={"amount": amount_cents, "token": token},
                   headers={"Authorization": f"Bearer {api_key}"}, timeout=10)
    r.raise_for_status()
    return r.json()
