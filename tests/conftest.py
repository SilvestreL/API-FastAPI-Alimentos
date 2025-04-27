import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.settings import settings


@pytest.fixture(scope="module")
def client():
    """Cliente de teste da aplicação FastAPI."""
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def get_token(client):
    """Autentica e retorna um token de acesso para o admin."""
    login_data = {
        "username": settings.FIRST_SUPERUSER,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }
    response = client.post("/api/v1/auth/login", data=login_data)
    assert response.status_code == 200
    token = response.json()["access_token"]
    return token
