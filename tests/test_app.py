import pytest
from flask import Flask
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_vowel_count(client):
    response = client.post('/vowel_count', json={'words': ['hello', 'world']})
    assert response.status_code == 200
    assert response.get_json() == {'hello': 2, 'world': 1}

    response = client.post('/vowel_count', json={})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid request format"}


def test_sort_words(client):
    response = client.post('/sort', json={'words': ['banana', 'apple', 'cherry'], 'order': 'asc'})
    assert response.status_code == 200
    assert response.get_json() == ['apple', 'banana', 'cherry']

    response = client.post('/sort', json={'words': ['banana', 'apple', 'cherry'], 'order': 'desc'})
    assert response.status_code == 200
    assert response.get_json() == ['cherry', 'banana', 'apple']

    response = client.post('/sort', json={})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid request format"}

    response = client.post('/sort', json={'words': ['banana', 'apple', 'cherry'], 'order': 'invalid'})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid order value"}
