from fastapi.testclient import TestClient

def test_health_check(client: TestClient):
    """
    Testa se o endpoint de health check está retornando o status correto
    e a estrutura de dados esperada.
    """
    response = client.get("/health")
    
    # Validações (Assertions)
    assert response.status_code == 200
    
    data = response.json()
    assert data["status"] == "healthy"
    assert "project_name" in data
    assert "environment" in data