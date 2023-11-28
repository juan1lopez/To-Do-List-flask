from app.models import Categoria
from app import db

class CategoriaRepository:
    def __init__(self):
        self.__model = Categoria

    def get_all(self) -> list[Categoria]:
        return db.session.query(self.__model).all()

    def get_by_id(self, id) -> Categoria:
        return db.session.query(self.__model).get(id)

    def create(self, entity: Categoria) -> Categoria:
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, id, t: Categoria) -> Categoria:
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
        categoria = self.get_by_id(id)
        db.session.delete(categoria)
        db.session.commit()
        return categoria