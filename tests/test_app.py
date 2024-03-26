from .conftest import client

def test_should_status_code_ok(client):
	response = client.get('/')
	assert response.status_code == 200
	assert response.content_type == 'text/html; charset=utf-8'

def test_calculator(client):
	response = client.get('/calculator?a=1&b=2')
	assert response.status_code == 200
	assert response.data == b'3'