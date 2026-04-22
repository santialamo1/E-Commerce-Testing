import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "https://fakestoreapi.com"

@pytest.fixture(scope="session")
def all_products(base_url):
    response = requests.get(f"{base_url}/products")
    return response.json()

@pytest.fixture(scope="session")
def token(base_url):
    credentials = {
        "username": "mor_2314",
        "password": "83r5^_"
    }
    response = requests.post(f"{base_url}/auth/login", json=credentials)
    return response.json()["token"]