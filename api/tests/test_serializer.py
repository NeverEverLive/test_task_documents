import pytest
from datetime import datetime

from ..models import Document, Right
from ..serializers import DocumentSchema, RightSchema


def test_document_serializer():
    data = {
        "name": "First document", 
        "text": "That was the first document"
    }


    new_document = Document(name=data['name'], text=data['text'])
    serializer = DocumentSchema()

    serializer_data = serializer.dump(new_document)
    serializer_data.pop('id')
    serializer_data.pop('inserted_at')
    serializer_data.pop('updated_at')

    assert serializer_data == data


def test_right_serializer():
    data = {
        "document_id": 3,
        "name": "First document", 
        "text": "That was the first document",
        "rights_from": "2022-06-07T19:55:58",
        "rights_to": "2022-06-07T19:56:45"
    }

    rights_from = datetime.strptime(data['rights_from'], "%Y-%m-%dT%H:%M:%S")
    rights_to = datetime.strptime(data['rights_to'], "%Y-%m-%dT%H:%M:%S")

    new_right = Right(name=data['name'], text=data['text'], document_id=data['document_id'], rights_from=rights_from, rights_to=rights_to)
    serializer = RightSchema()
    
    serializer_data = serializer.dump(new_right)
    serializer_data.pop('id')
    serializer_data.pop('inserted_at')
    serializer_data.pop('updated_at')

    print(serializer_data)
    print(data)

    assert serializer_data == data
