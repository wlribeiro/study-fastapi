from http import client
from urllib import response
from starlette.testclient import TestClient


from main import app

client = TestClient(app)

def test_main_status_code():
    response = client.get("/")
    assert response.status_code == 200

def test_main_response_json():
    response = client.get("/")
    assert response.json() == {"hello": "world"}

def test_listar_to_do_response_json():
    response = client.get("/to-do")
    assert len(response.json()) == 3