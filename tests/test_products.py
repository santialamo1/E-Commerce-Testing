import pytest
import requests

@pytest.mark.products
def test_all_products_results(all_products):
    assert len(all_products) > 0

@pytest.mark.products
def test_products_have_required_fields(all_products):
    for product in all_products:
        assert "id" in product
        assert "title" in product
        assert "price" in product
        assert "category" in product

@pytest.mark.products
def test_products_price_is_positive(all_products):
    for product in all_products:
        assert product["price"] > 0

@pytest.mark.products
def test_get_single_product(all_products, base_url):
    response = requests.get(f"{base_url}/products/1")
    product = response.json()

    assert response.status_code == 200
    assert product["id"] == 1

@pytest.mark.products
def test_get_nonexistent_product(all_products, base_url):
    response = requests.get(f"{base_url}/products/9999")

    assert response.status_code == 200

@pytest.mark.products
@pytest.mark.parametrize ("category", ["electronics", "jewelery", "men's clothing", "women's clothing"])

def test_category_returns_products(all_products, base_url, category):
    response = requests.get(f"{base_url}/products/category/{category}")
    product = response.json()

    assert response.status_code == 200
    assert len(product) > 0
    for product in product:
        assert product["category"] == category