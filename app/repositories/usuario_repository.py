from app.models import Usuario
from app import db

class UsuarioRepository:
    def __init__(self):
        self.__model = Usuario

    def get_all(self) -> list[Usuario]:
        return db.session.query(self.__model).all()

    def get_by_id(self, id) -> Usuario:
        return db.session.query(self.__model).get(id)

    def create(self, entity: Usuario) -> Usuario:
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, id, t: Usuario) -> Usuario:
        entity = self.get_by_id(id)
        entity.fecha = t.fecha
        entity.duracion = t.duracion
        entity.descripcion = t.descripcion
        entity.creador_id = t.creador_id
        entity.ejecutante_id = t.ejecutante_id
        entity.categoria_id = t.categoria_id
        entity.estado_id = t.estado_id
        db.session.add(entity)
        db.session.commit()
        return entity

    def delete(self, id)-> bool:
        usuario = self.get_by_id(id)
        db.session.delete(usuario)
        db.session.commit()
        return usuario