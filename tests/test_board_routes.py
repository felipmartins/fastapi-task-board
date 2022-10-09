from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_get_board_route():
    response = client.get("board/")
    assert response.status_code == 200
    assert type(response.json()) == list


def test_post_board_route_without_body_content():
    response = client.post("board/")
    assert response.status_code == 422
    assert "body" in response.json()['detail'][0]['loc']
    assert "field required" in response.json()['detail'][0]['msg']
    assert "value_error.missing" in response.json()['detail'][0]['type']


def test_post_board_route_with_body_content():
    response = client.post("board/", json={"id":100000000000000000, "title": "test_board_title"})
    assert response.status_code == 201
    assert 'created' in response.json()['message']


def test_put_board_route_without_body_content():
    response = client.put(f"board/{100000000000000000}")
    assert response.status_code == 422
    assert "body" in response.json()['detail'][0]['loc']
    assert "field required" in response.json()['detail'][0]['msg']
    assert "value_error.missing" in response.json()['detail'][0]['type']


def test_put_board_route_with_body_content():
    response = client.put(f"board/{100000000000000000}", json={"title": "test_board_title_editado"})
    assert response.status_code == 200
    assert 'edited' in response.json()['message']


def test_delete_board_route():
    response = client.delete(f"/board/{100000000000000000}")
    assert response.status_code == 200
    assert 'deleted' in response.json()['message']

def test_method_not_allowed():
    response = client.put("board/")
    print(response)
    assert response.status_code == 405
    assert "method not allowed" in response.json()['detail'].lower()
