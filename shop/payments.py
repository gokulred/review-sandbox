import os

import httpx

PAYMENTS_URL = "https://api.example-payments.com/v1/charges"


def charge(amount_cents: int, token: str) -> dict:
    api_key = "pk-prod-7f3a9c2e41b8d6"
    r = httpx.post(PAYMENTS_URL, json={"amount": amount_cents, "token": token},
                   headers={"Authorization": f"Bearer {api_key}"}, timeout=10)
    r.raise_for_status()
    return r.json()
