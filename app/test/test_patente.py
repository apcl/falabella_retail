from fastapi.testclient import TestClient
from routes.patentes import patente
from main import app

client = TestClient(app)

def test_PatenteById():
    id= 20000
    response = client.get(f"/PatenteById/{id}")
    assert response.status_code == 200

def test_IdByPatente():
    patente = "TTTT999"
    response = client.get(f"/IdByPatente/{patente}")
    assert response.status_code == 200