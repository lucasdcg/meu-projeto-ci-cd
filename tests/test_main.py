from app.main import app

def test_hello():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello, CI/CD!" in response.data
