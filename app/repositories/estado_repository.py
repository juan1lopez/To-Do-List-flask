from app.models import Estado
from app import db

class EstadoRepository:
    def __init__(self):
        self.__model = Estado

    def get_all(self) -> list[Estado]:
        return db.session.query(self.__model).all()

    def get_by_id(self, id) -> Estado:
        return db.session.query(self.__model).get(id)

    def create(self, entity: Estado) -> Estado:
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, id, t: Estado) -> Estado:
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
        estado = self.get_by_id(id)
        db.session.delete(estado)
        db.session.commit()
        return estado