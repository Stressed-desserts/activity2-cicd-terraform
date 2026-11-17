import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_status(client):
    res = client.get("/")
    assert res.status_code == 200

def test_home_payload(client):
    res = client.get("/")
    data = res.get_json()
    assert data["service"] == "activity2-web-api"
    assert data["version"] == "2.0.0"

def test_api_status_code(client):
    res = client.get("/api/status")
    assert res.status_code == 200

def test_api_status_payload(client):
    res = client.get("/api/status")
    data = res.get_json()
    assert data["activity"] == "Activity 2"
    assert data["status"] == "operational"
