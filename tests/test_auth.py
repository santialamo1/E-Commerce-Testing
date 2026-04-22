import pytest
import requests
from config import HEADERS

@pytest.mark.auth
def test_login_succesful(base_url):
    response = requests.post(f"{base_url}/auth/login", json={"username": "mor_2314", "password": "83r5^_"}, headers=HEADERS)
    user = response.json()

    assert response.status_code in [200, 201]
    assert "token" in user
    assert len(user["token"]) > 0

@pytest.mark.auth
def test_login_returns_string(base_url, token):
    response = requests.post(f"{base_url}/auth/login", json={"username": "mor_2314", "password": "83r5^_"}, headers=HEADERS)
    user = response.json()

    assert isinstance(user["token"], str)

@pytest.mark.auth
def test_login_invalid_credentials(base_url):
    response = requests.post(f"{base_url}/auth/login", json={"username": "mor_2315", "password": "83r5bg"}, headers=HEADERS)

    assert response.status_code != 200

@pytest.mark.auth
def test_login_missing_password(base_url):
    response = requests.post(f"{base_url}/auth/login", json={"username": "mor_2314", "password": ""}, headers=HEADERS)

    assert response.status_code != 200
