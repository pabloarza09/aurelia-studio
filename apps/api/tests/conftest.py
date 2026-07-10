"""Pytest configuration and fixtures."""

import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client():
    """Create a test client."""
    return TestClient(app)


@pytest.fixture
def api_url():
    """Base API URL for tests."""
    return "http://testserver"
