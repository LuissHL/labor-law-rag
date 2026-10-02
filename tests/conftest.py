import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client() -> TestClient:
    """
    Fixture que fornece um TestClient configurado com a aplicação FastAPI.
    Será injetado automaticamente nas funções de teste que pedirem 'client'.
    """
    with TestClient(app) as test_client:
        yield test_client