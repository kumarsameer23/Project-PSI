import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.security import create_token

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def token():
    return create_token("test@example.com")

@pytest.fixture
def auth_headers(token):
    return {"Authorization": f"Bearer {token}"}
