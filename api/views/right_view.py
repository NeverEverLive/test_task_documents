from flask import Blueprint, jsonify, request
from sqlalchemy import inspect


from ..models import Right
from main import db
from ..serializers import RightSchema


rights = Blueprint('rights', __name__)


@rights.get('/rights')
def get_all_rights():
    try:
        rights = Right.get_all()
        
        serializer = RightSchema(many=True)
        data = serializer.dump(rights)
        print(data)
    except Exception as error:
        return jsonify(str(error))
    return jsonify(data)


@rights.get('/rights/<int:id>')
def get_right(id):
    right = Right.get_by_id(id)

    serializer = RightSchema()
    data = serializer.dump(right)

    return jsonify(data)


@rights.post('/rights/add')
def create_right():
    data = request.get_json()

    new_right = Right(**data)
    new_right.save()
    
    serializer = RightSchema()
    data = serializer.dump(new_right)

    return jsonify(data), 201


@rights.put('/rights/update')
def update_right():
    data = request.get_json()
    if not data.get('id'):
        return jsonify({"message": "Need 'id' atribute for update"}), 500

    id = data.get('id')
    right_to_update = Right.get_by_id(id)

    mapper = inspect(Right)
    attrs = [column.key for column in mapper.attrs]

    for attr, value in data.items():
        if attr in attrs:
            setattr(right_to_update, attr, value)
    
    db.session.commit()

    serializer = RightSchema()
    right_data = serializer.dump(right_to_update)

    return jsonify(right_data), 200
    

@rights.delete('/rights/delete')
def delete_right():
    data = request.get_json()
    if not data.get('id'):
        return jsonify({"message": "Need 'id' atribute for update"}), 500

    id = data.get('id')
    right_to_delete = Right.get_by_id(id)
    right_to_delete.delete()

    return jsonify({"message": "Deleted"}), 204