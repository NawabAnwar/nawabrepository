import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Test the API root route return status and content."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"CloudKart E-Commerce Platform" in response.data

def test_health_check_endpoint(client):
    """Test system health check for automated deployment readiness."""
    response = client.get('/health')
    assert response.status_code == 200
    assert b"healthy" in response.data
