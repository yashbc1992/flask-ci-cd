from app import app

def test_hello():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Hello, Jenkins CI/CD!" in response.data
