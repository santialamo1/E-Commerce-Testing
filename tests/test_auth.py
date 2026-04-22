import pytest
import requests

@pytest.mark.auth
def test_login_succesful(base_url):
    response = requests.post(f"{base_url}/auth/login", json={"username": "emilys", "password": "emilyspass"})
    user = response.json()

    assert response.status_code in [200, 201]
    assert "accessToken" in user
    assert len(user["accessToken"]) > 0

@pytest.mark.auth
def test_login_returns_string(base_url):
    response = requests.post(f"{base_url}/auth/login", json={"username": "emilys", "password": "emilyspass"})
    user = response.json()

    assert isinstance(user["accessToken"], str)

@pytest.mark.auth
def test_login_invalid_credentials(base_url):
    response = requests.post(f"{base_url}/auth/login", json={"username": "mor_2315", "password": "83r5bg"})

    assert response.status_code != 200

@pytest.mark.auth
def test_login_missing_password(base_url):
    response = requests.post(f"{base_url}/auth/login", json={"username": "emilys", "password": ""})

    assert response.status_code != 200
