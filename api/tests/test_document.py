import pytest
import requests
import json


def test_get_documents():
    url = 'http://localhost:5000/document'
    response = requests.get(url)
    assert response.status_code == 200, "Status code isn't 200"


def test_get_document():
    url = 'http://localhost:5000/document/2'
    response = requests.get(url)
    assert response.status_code == 200, "Status code isn't 200"
    assert response.json()['id'] == 2


def test_post_document():
    url = 'http://localhost:5000/document/add'
    input_json = {
        "name": "Test document",
        "text": "Test Text"
    }

    response = requests.post(url, json=input_json)

    assert response.status_code == 201
    assert response.json()['name'] == 'Test document'
    assert response.json()['text'] == 'Test Text'

    response = requests.delete('http://localhost:5000/document/delete', json={"id": response.json()['id']})


def test_put_document():
    url = 'http://localhost:5000/document/update'
    input_json = {
        "id": 3,
        "name": "Test document!"
    }

    response = requests.put(url, json=input_json)

    assert response.status_code == 200
    assert response.json()['name'] == input_json['name']
    assert response.json()['id'] == 3


def test_delete_document():

    url = 'http://localhost:5000/document/add'
    input_json = {
        "name": "Test document",
        "text": "Test Text"
    }

    response = requests.post(url, json=input_json)

    url = f'http://localhost:5000/document/{response.json()["id"]}'
    document_for_delete = requests.get(url)

    url = 'http://localhost:5000/document/delete'

    response = requests.delete(url, json={"id": response.json()['id']})

    after_delete_data = requests.get('http://localhost:5000/document').json()

    assert response.status_code == 204
    assert document_for_delete.json() not in after_delete_data
