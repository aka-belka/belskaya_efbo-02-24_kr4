import pytest
from faker import Faker

fake = Faker()

@pytest.mark.asyncio
async def test_create_user_success(client):
    username = fake.user_name()
    age = fake.random_int(18, 80)
    response =  await client.post("/users/", json = {"username": username, "age": age})
    assert response.status_code == 201
    assert response.json()["data"]["username"] == username
    assert response.json()["data"]["age"] == age
    assert "id" in response.json()["data"]

@pytest.mark.asyncio
async def test_create_user_fail_age(client):
    response = await client.post("/users/", json={"username": "Oleg"})
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_create_user_fail_username(client):
    response = await client.post("/users/", json={"age": 60})
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_get_user_success(client):
    username = fake.user_name()
    age = fake.random_int(18, 80)
    create_response = await client.post("/users/", json={"username": username, "age": age})
    user_id = create_response.json()["data"]["id"]
    response = await client.get(f"/users/{user_id}/")
    assert response.status_code == 200
    assert response.json()["username"] == username
    assert response.json()["age"] == age

@pytest.mark.asyncio
async def test_get_user_fail(client):
    response = await client.get("/users/10/")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

@pytest.mark.asyncio
async def test_get_user_fail_type(client):
    response = await client.get("/users/abc/")
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_delete_user_success(client):
    username = fake.user_name()
    age = fake.random_int(18, 80)
    create_response = await client.post("/users/", json={"username": username, "age": age})
    user_id = create_response.json()["data"]["id"]
    response = await client.delete(f"/users/{user_id}/")
    assert response.status_code == 204

    get_response = await client.get(f"/users/{user_id}/")
    assert get_response.status_code == 404

@pytest.mark.asyncio
async def test_delete_user_fail(client):
    response = await client.delete("/users/10/")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

@pytest.mark.asyncio
async def test_delete_user_fail_twice(client):
    username = fake.user_name()
    age = fake.random_int(18, 80)
    create_response = await client.post("/users/", json={"username": username, "age": age})
    user_id = create_response.json()["data"]["id"]
    await client.delete(f"/users/{user_id}/")
    response = await client.delete(f"/users/{user_id}/")
    assert response.status_code == 404