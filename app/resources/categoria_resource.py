from flask import jsonify, Blueprint, request
from app.mapping import CategoriaSchema
from app.services import CategoriaService

categoria = Blueprint('categoria', __name__)
service = CategoriaService()
usurario_schema=CategoriaSchema()

"""
Obtiene todos los categorias
"""
@categoria.route('/', methods=['GET'])
def all():
    resp = categoria_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene una categoria por id
"""
@categoria.route('/<int:id>', methods=['GET'])
def one(id):
    resp = categoria_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea nueva categoria
"""
@categoria.route('/', methods=['POST'])
def create():
    categoria = categoria_schema.load(request.json)
    resp = categoria_schema.dump(service.create(categoria))
    return resp, 201

"""
Actualiza una categoria existente
"""
@categoria.route('/<int:id>', methods=['PUT'])
def update(id):
    categoria = categoria_schema.load(request.json)
    resp = categoria_schema.dump(service.update(id, categoria))
    return resp, 200

"""
Elimina una categoria existente
"""
@categoria.route('/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "categoria eliminada correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar la categoria"
    return jsonify(msg), 204