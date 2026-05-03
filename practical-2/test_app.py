import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test main endpoint returns 200 and correct JSON."""
    resp = client.get('/')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['practical'] == 'DevOps Practical No. 2'
    assert data['author'] == 'Nilesh Malekar'

def test_health(client):
    """Test health endpoint returns healthy status."""
    resp = client.get('/health')
    assert resp.status_code == 200
    assert resp.get_json()['status'] == 'healthy'

def test_info(client):
    """Test info endpoint returns deployment info."""
    resp = client.get('/info')
    assert resp.status_code == 200
    data = resp.get_json()
    assert 'python' in data
    assert 'hostname' in data
