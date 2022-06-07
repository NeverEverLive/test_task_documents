import pytest
import requests
import json


def test_get_rights():
    url = 'http://localhost:5000/rights'
    response = requests.get(url)
    assert response.status_code == 200, "Status code isn't 200"


def test_get_right():
    url = 'http://localhost:5000/rights/6'
    response = requests.get(url)
    assert response.status_code == 200, "Status code isn't 200"
    assert response.json()['id'] == 6


def test_post_right():
    url = 'http://localhost:5000/rights/add'
    input_json = {
        "document_id": 3,
        "name": "Test right",
        "text": "Test Text",
        "rights_from": "2022-06-07T19:55:58",
        "rights_to": "2022-06-07 19:56:45"
    }

    response = requests.post(url, json=input_json)
    print(response.reason)
    assert response.status_code == 201
    assert response.json()['name'] == 'Test right'
    assert response.json()['text'] == 'Test Text'

    response = requests.delete('http://localhost:5000/rights/delete', json={"id": response.json()['id']})


def test_put_right():
    url = 'http://localhost:5000/rights/update'
    input_json = {
        "id": 6,
        "name": "Test right!"
    }

    response = requests.put(url, json=input_json)

    assert response.status_code == 200
    assert response.json()['name'] == input_json['name']
    assert response.json()['id'] == 6


def test_delete_right():

    url = 'http://localhost:5000/rights/add'
    input_json = {
        "document_id": 3,
        "name": "Test right",
        "text": "Test Text",
        "rights_from": "2022-06-07T19:55:58",
        "rights_to": "2022-06-07 19:56:45"
    }

    response = requests.post(url, json=input_json)

    url = f'http://localhost:5000/rights/{response.json()["id"]}'
    right_for_delete = requests.get(url)

    url = 'http://localhost:5000/rights/delete'

    response = requests.delete(url, json={"id": response.json()['id']})

    after_delete_data = requests.get('http://localhost:5000/rights').json()

    assert response.status_code == 204
    assert right_for_delete.json() not in after_delete_data
