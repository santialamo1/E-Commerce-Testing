import pytest
import requests
from config import HEADERS

@pytest.mark.cart
def test_get_all_carts_status_ok(base_url):
    response = requests.get(f"{base_url}/carts", headers=HEADERS)
    carts = response.json()
    
    assert response.status_code == 200
    assert len(carts) > 0

@pytest.mark.cart
def test_cart_has_required_fields(base_url):
    response = requests.get(f"{base_url}/carts/1", headers=HEADERS)
    cart = response.json()

    assert "id" in cart
    assert "userId" in cart
    assert "products" in cart

@pytest.mark.cart
def test_get_carts_by_user(base_url):
    response = requests.get(f"{base_url}/carts/user/1", headers=HEADERS)
    carts = response.json()

    assert response.status_code in [200, 201]
    for cart in carts:
        assert cart["userId"] == 1

@pytest.mark.cart
def test_create_cart(base_url):
    response = requests.post(f"{base_url}/carts", json={"userId": 1, "products": [{"productId": 1, "quantity": 2}]}, headers=HEADERS)
    carts = response.json()

    assert response.status_code in [200, 201]
    assert "id" in carts