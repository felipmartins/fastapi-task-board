import pytest
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)


@pytest.mark.order(before="test_board_routes.py::test_delete_board_route")
def test_get_tasks_route():
    response = client.get(f"board/{100000000000000000}")
    assert response.status_code == 200
    assert type(response.json()) == list


@pytest.mark.order(after="test_get_tasks_route")
def test_post_task_route_without_body_content():
    response = client.post(f"board/{100000000000000000}")
    assert response.status_code == 422
    assert "body" in response.json()['detail'][0]['loc']
    assert "field required" in response.json()['detail'][0]['msg']
    assert "value_error.missing" in response.json()['detail'][0]['type']


@pytest.mark.order(after="test_post_task_route_without_body_content")
def test_post_task_route_with_body_content():
    response = client.post(f"board/{100000000000000000}", json={"id":100000000000000000, "title": "string", "description": "string"})
    assert response.status_code == 201
    assert 'created' in response.json()['message']


@pytest.mark.order(after="test_post_task_route_with_body_content")
def test_put_task_route_without_body_content():
    response = client.put(f"board/{100000000000000000}/{100000000000000000}")
    assert response.status_code == 422
    assert "body" in response.json()['detail'][0]['loc']
    assert "field required" in response.json()['detail'][0]['msg']
    assert "value_error.missing" in response.json()['detail'][0]['type']


@pytest.mark.order(after="test_put_task_route_without_body_content")
def test_put_task_route_with_body_content():
    response = client.put(f"board/{100000000000000000}/{100000000000000000}", json={ "title": "string_editada", "description": "string_editada"})
    assert response.status_code == 200
    assert 'edited' in response.json()['message']


@pytest.mark.order(after="test_method_not_allowed")
def test_delete_task_route():
    response = client.delete(f"board/{100000000000000000}/{100000000000000000}")
    assert response.status_code == 200
    assert 'deleted' in response.json()['message']


@pytest.mark.order(after="test_put_task_route_with_body_content")
def test_method_not_allowed():
    response = client.post(f"board/{100000000000000000}/{100000000000000000}")
    assert response.status_code == 405
    assert "method not allowed" in response.json()['detail'].lower()
