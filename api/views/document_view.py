from flask import Blueprint, jsonify, request
from sqlalchemy import inspect

from ..models import Document
from main import db
from ..serializers import DocumentSchema


documents = Blueprint('documents', __name__)


@documents.get('/document')
def get_all_documents():
    try:
        documents = Document.get_all()
        
        serializer = DocumentSchema(many=True)
        data = serializer.dump(documents)
        print(data)
    except Exception as error:
        return jsonify(str(error))
    return jsonify(data)


@documents.get('/document/<int:id>')
def get_document(id):
    document = Document.get_by_id(id)

    serializer = DocumentSchema()
    data = serializer.dump(document)

    return jsonify(data)


@documents.post('/document/add')
def create_document():
    data = request.get_json()
    
    new_document = Document(**data)
    new_document.save()
    
    serializer = DocumentSchema()
    data = serializer.dump(new_document)

    return jsonify(data), 201


@documents.put('/document/update')
def update_document():
    data = request.get_json()
    if not data.get('id'):
        return jsonify({"message": "Need 'id' atribute for update"}), 500

    id = data.get('id')
    document_to_update = Document.get_by_id(id)

    mapper = inspect(Document)
    attrs = [column.key for column in mapper.attrs]

    for attr, value in data.items():
        if attr in attrs:
            setattr(document_to_update, attr, value)
    
    db.session.commit()

    serializer = DocumentSchema()
    document_data = serializer.dump(document_to_update)

    return jsonify(document_data), 200
    

@documents.delete('/document/delete')
def delete_document():
    data = request.get_json()
    if not data.get('id'):
        return jsonify({"message": "Need 'id' atribute for update"}), 500

    id = data.get('id')
    document_to_delete = Document.get_by_id(id)
    document_to_delete.delete()

    return jsonify({"message": "Deleted"}), 204
