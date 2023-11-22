
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_search_success():
    response = client.get("/search?query=test")
    assert response.status_code == 200
    assert "results" in response.json()

def test_search_failure():
    response = client.get("/search?query=")
    assert response.status_code == 422  # Validation error for empty query
