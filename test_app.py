from app import app

def test_quote_endpoint():
    tester = app.test_client()
    response = tester.get('/quote')
    assert response.status_code == 200
    assert 'quote' in response.get_json()
