from flask import Blueprint
from .models import Document
from .serializers import DocumentSchema

view = Blueprint('views', __name__)

@view.route('/')
def dummy_request():
    return {"message": "Hello world"}


@view.get('/documents', methods=['GET'])
def get_all_documents():
    pass


@view.post('/documents', methods=['POST'])
def create_documents():
    pass


@view.put('/documents/<int:id>', methods=['GET'])
def update_documents(id):
    pass


@view.put('/documents', methods=['PUT'])
def update_documents(request):
    pass