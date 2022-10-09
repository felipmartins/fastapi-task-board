from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_home_route():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"info": "this is the index route of the task board API, use /board to interact with boards and /board/{id} to retrieve all tasks associated with the chosen board"}