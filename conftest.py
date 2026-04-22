# conftest.py

import pytest
import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

@pytest.fixture(scope="session")
def base_url():
    return "https://fakestoreapi.com"

@pytest.fixture(scope="session")
def all_products(base_url):
    response = requests.get(f"{base_url}/products", headers=HEADERS)
    return response.json()

@pytest.fixture(scope="session")
def token(base_url):
    credentials = {
        "username": "mor_2314",
        "password": "83r5^_"
    }
    response = requests.post(f"{base_url}/auth/login", json=credentials, headers=HEADERS)
    return response.json()["token"]