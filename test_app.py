import pytest
from app import app  

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to My First Flask App" in response.data

def test_info_route(client):
    response = client.get('/info')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["developer"] == "Pradeep Rawat"
    assert json_data["project"] == "My First Flask App"

def test_form_submission(client):
    response = client.post('/submit', data={
        'name': 'Test User',
        'message': 'Hello from test!'
    })
    assert response.status_code == 200
    assert b"Thanks, Test User!" in response.data
