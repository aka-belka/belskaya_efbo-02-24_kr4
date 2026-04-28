from fastapi.testclient import TestClient
from my_app.main import app
import pytest

@pytest.fixture
def client():
    return TestClient(app)