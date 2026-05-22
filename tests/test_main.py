from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_hello_returns_greeting():
    response = client.get("/hello")
    assert response.status_code == 200
    assert "Hello from myapp" in response.text


def test_health_returns_up():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "UP"}
