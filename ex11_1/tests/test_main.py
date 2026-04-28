import pytest

def test_create_user_success(client):
    response = client.post("/users/", json = {"username": "Valera", "age": 19})
    assert response.status_code == 200
    assert response.json()["data"]["username"] == "Valera"
    assert response.json()["data"]["age"] == 19
    assert "id" in response.json()["data"]

def test_create_user_fail_age(client):
    response = client.post("/users/", json={"username": "Oleg"})
    assert response.status_code == 422

def test_create_user_fail_username(client):
    response = client.post("/users/", json={"age": 60})
    assert response.status_code == 422

def test_get_user_success(client):
    response = client.post("/users/", json={"username": "Igor", "age": 45})
    user_id = response.json()["data"]["id"]
    response = client.get(f"/users/{user_id}/")
    assert response.status_code == 200
    assert response.json()["username"] == "Igor"
    assert response.json()["age"] == 45

def test_get_user_fail(client):
    response = client.get("/users/10/")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

def test_get_user_fail_type(client):
    response = client.get("/users/abc/")
    assert response.status_code == 422

def test_delete_user_success(client):
    response = client.post("/users/", json={"username": "Dasha", "age": 15})
    user_id = response.json()["data"]["id"]
    response = client.delete(f"/users/{user_id}/")
    assert response.status_code == 200
    assert response.json()["message"] == "Delete successfully!"

    response = client.get(f"/users/{user_id}/")
    assert response.status_code == 404

def test_delete_user_fail(client):
    response = client.delete("/users/10/")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_delete_user_fail_twice(client):
    response = client.post("/users/", json={"username": "Sasha", "age": 25})
    user_id = response.json()["data"]["id"]
    client.delete(f"/users/{user_id}/")
    response = client.delete(f"/users/{user_id}/")
    assert response.status_code == 404