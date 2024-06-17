import pytest
# Garantir que o python encontre o módulo src
from src.__init__ import create_app

app = create_app()


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_vowel_count(client):
    response = client.post(
        '/vowel_count', json={'words': ['hello', 'cassação', 'aati']})
    assert response.status_code == 200
    assert response.get_json() == {'hello': 2, 'cassação': 4, 'aati': 3}

    response = client.post('/vowel_count', json={})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid request format"}

    response = client.post('/vowel_count', json={'words': ['casa', [], 5]})
    assert response.status_code == 400
    assert response.get_json() == {"error": "All elements in 'words' must be strings"}


def test_sort_words(client):
    response = client.post(
        '/sort', json={'words': ['banana', 'apple', 'cherry'], 'order': 'asc'})
    assert response.status_code == 200
    assert response.get_json() == ['apple', 'banana', 'cherry']

    response = client.post(
        '/sort', json={'words': ['banana', 'apple', 'cherry'], 'order': 'desc'})
    assert response.status_code == 200
    assert response.get_json() == ['cherry', 'banana', 'apple']

    response = client.post('/sort', json={})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid request format"}

    response = client.post(
        '/sort', json={'words': ['banana', 'apple', 'cherry'], 'order': 'invalid'})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid order option"}

    response = client.post(
        '/sort', json={'words': ['banana', 'apple', 'cherry']})
    assert response.status_code == 200
    assert response.get_json() == ['apple', 'banana', 'cherry']


def test_404_not_found(client):
    response = client.get('/non_existent_route')
    assert response.status_code == 404
    assert response.get_json() == {"error": "Resource not found"}


def test_405_method_not_allowed(client):
    response = client.get('/vowel_count')
    assert response.status_code == 405
    assert response.get_json() == {"error": "Method not allowed"}
