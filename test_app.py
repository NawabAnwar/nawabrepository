import pytest
from app import application

@pytest.fixture
def api_client():
    """Configure test environment and yield Flask test client."""
    application.config['TESTING'] = True
    with application.test_client() as runner:
        yield runner

def test_root_route_success(api_client):
    """Verify root endpoint returns HTTP 200 and expected service payload."""
    result = api_client.get('/')
    assert result.status_code == 200
    assert b"CloudKart Core Engine" in result.data

def test_health_check_status(api_client):
    """Verify health check endpoint reports operational status."""
    result = api_client.get('/health')
    assert result.status_code == 200
    json_data = result.get_json()
    assert json_data['status'] == 'healthy'
    assert json_data['database_connection'] == 'active'
