from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_history_empty():
    response = client.get("/api/v1/history")
    assert response.status_code == 200
    assert response.json() == []

def test_get_history_success():
    client.post("/api/v1/calculate", json={
        "operation": "ADDITION",
        "x": 5,
        "y": 5
    })

    response = client.get("/api/v1/history")
    
    # This fails now (404)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)



