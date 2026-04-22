import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "https://dummyjson.com"

@pytest.fixture(scope="session")
def all_products(base_url):
    response = requests.get(f"{base_url}/products")
    return response.json()["products"]  

@pytest.fixture(scope="session")
def token(base_url):
    credentials = {
        "username": "emilys",
        "password": "emilyspass"
    }
    response = requests.post(f"{base_url}/auth/login", json=credentials)
    return response.json()["accessToken"]  