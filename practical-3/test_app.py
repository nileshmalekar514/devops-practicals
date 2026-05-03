import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_status(client):
    """Test that index returns 200."""
    resp = client.get('/')
    assert resp.status_code == 200

def test_index_content(client):
    """Test index returns correct practical info."""
    data = client.get('/').get_json()
    assert data['practical'] == 'DevOps Practical No. 3'
    assert data['author'] == 'Nilesh Malekar'
    assert 'GitHub Actions' in data['ci']

def test_health(client):
    """Test health endpoint returns healthy."""
    resp = client.get('/health')
    assert resp.status_code == 200
    assert resp.get_json()['status'] == 'healthy'

def test_info(client):
    """Test info endpoint returns CI tool name."""
    data = client.get('/info').get_json()
    assert data['ci_tool'] == 'GitHub Actions'
    assert 'python' in data
