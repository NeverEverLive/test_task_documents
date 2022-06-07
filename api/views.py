from flask import Blueprint, jsonify, request
from sqlalchemy import inspect


from .models import Document
from main import db
from .serializers import DocumentSchema

view = Blueprint('views', __name__)

@view.route('/')
def dummy_request():
    return {"message": "Hello world"}


@view.get('/documents')
def get_all_documents():
    try:
        documents = Document.get_all()
        
        serializer = DocumentSchema(many=True)
        data = serializer.dump(documents)
        print(data)
    except Exception as error:
        return jsonify(str(error))
    return jsonify(data)


@view.get('/documents/<int:id>')
def get_document(id):
    document = Document.get_by_id(id)

    serializer = DocumentSchema()
    data = serializer.dump(document)

    return jsonify(data)


@view.post('/documents/add')
def create_documents():
    data = request.get_json()

    new_document = Document(**data)
    new_document.save()
    
    serializer = DocumentSchema()
    data = serializer.dump(new_document)

    return jsonify(data), 201




@view.put('/documents/update')
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
    

@view.delete('/documents/delete')
def delete_document():
    data = request.get_json()
    if not data.get('id'):
        return jsonify({"message": "Need 'id' atribute for update"}), 500

    id = data.get('id')
    document_to_delete = Document.get_by_id(id)
    document_to_delete.delete()

    return jsonify({"message": "Deleted"}), 204


@view.errorhandler(404)
def not_found_error(error):
    return jsonify({"message": "Resource not found"})

@view.errorhandler(500)
def internal_server(error):
    return jsonify({"message": str(error)})
