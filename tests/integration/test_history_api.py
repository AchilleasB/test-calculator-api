from fastapi.testclient import TestClient
from app.main import app
from app.api.v1.calculator import repository
import pytest

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_history():
    repository.clear()
    yield

def test_get_history_empty():
    response = client.get("/api/v1/history")
    assert response.status_code == 200
    assert response.json() == {"records": []}

def test_get_history_success():
    client.post("/api/v1/calculate", json={
        "operation": "addition",
        "x": 5,
        "y": 5
    })

    response = client.get("/api/v1/history")
   
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["records"], list)
    assert len(data["records"]) == 1
    record = data["records"][0]
    # Check start of summary string to match expected format (ignoring timestamp at end)
    expected_prefix = "5.0 and 5.0 were operated with addition and the result is 10.0, at "
    assert record["summary"].startswith(expected_prefix)



