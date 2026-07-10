"""Health check endpoint tests."""

import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.mark.unit
class TestHealth:
    """Health check tests."""

    def test_health_check(self):
        """Test health check endpoint."""
        client = TestClient(app)
        response = client.get("/api/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"

    def test_readiness_check(self):
        """Test readiness check endpoint."""
        client = TestClient(app)
        response = client.get("/api/ready")
        assert response.status_code == 200
        assert response.json()["ready"] is True

    def test_root_endpoint(self):
        """Test root endpoint."""
        client = TestClient(app)
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["app"] == "Aurelia OS API"
        assert data["status"] == "running"
