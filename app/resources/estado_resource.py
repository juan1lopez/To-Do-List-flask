from flask import jsonify, Blueprint, request
from app.mapping import EstadoSchema
from app.services import EstadoService

estado = Blueprint('estado', __name__)
service = EstadoService()
estado_schema = EstadoSchema()

"""
Obtiene todas los estados
"""
@estado.route('/', methods=['GET'])
def all():
    resp = estado_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene una estado por id
"""
@estado.route('/<int:id>', methods=['GET'])
def one(id):
    resp = estado_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea nueva estado
"""
@estado.route('/', methods=['POST'])
def create():
    estado = estado_schema.load(request.json)
    resp = estado_schema.dump(service.create(estado))
    return resp, 201

"""
Actualiza una estado existente
"""
@estado.route('/<int:id>', methods=['PUT'])
def update(id):
    estado = estado_schema.load(request.json)
    resp = estado_schema.dump(service.update(id, estado))
    return resp, 200

"""
Elimina una estado existente
"""
@estado.route('/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "estado eliminada correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar la estado"
    return jsonify(msg), 204