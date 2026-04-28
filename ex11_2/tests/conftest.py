import pytest
from httpx import AsyncClient, ASGITransport
from my_app.main import app, users

@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client

@pytest.fixture(autouse=True)
def clean_users():
    users.clear()
    yield
    users.clear()