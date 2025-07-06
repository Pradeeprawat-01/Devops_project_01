import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Pradeep Singh Rawat | Portfolio" in response.data  # Robust check

def test_info(client):
    response = client.get('/info')
    assert response.status_code == 200
    data = response.get_json()
    assert data["developer"] == "Pradeep Singh Rawat"

def test_form_submission(client):
    response = client.post('/submit', data={
        'name': 'Test User',
        'message': 'Hello from test!'
    })
    assert response.status_code == 200
    assert b'Thank you, Test User' in response.data
