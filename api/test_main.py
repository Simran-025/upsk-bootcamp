from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_team():
    response = client.post("/teams/", json={"name": "Testing Team"})
    assert response.status_code == 200
    assert response.json()["name"] == "Testing Team"

def test_create_user():
    response = client.post("/users/", json={"name": "Test User", "email": "test@example.com"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
