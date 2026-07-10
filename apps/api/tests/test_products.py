"""Tests for product service."""

import pytest
from fastapi.testclient import TestClient


@pytest.mark.unit
class TestProducts:
    """Product service tests."""

    def test_create_product(self, client, user_token):
        """Test product creation."""
        response = client.post(
            "/products/",
            json={
                "name": "Test Product",
                "description": "A test product",
                "price": 29.99,
                "status": "active",
            },
            headers={"Authorization": f"Bearer {user_token}"},
        )
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Test Product"
        assert data["price"] == 29.99

    def test_list_products(self, client, user_token):
        """Test listing products."""
        response = client.get(
            "/products/",
            headers={"Authorization": f"Bearer {user_token}"},
        )
        assert response.status_code == 200
        assert isinstance(response.json(), list)
