from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/utils/health")
    assert response.status_code == 200
    assert response.json() == {'status': "ok"}
