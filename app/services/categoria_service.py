
from app.models import Categoria
from app.repositories import CategoriaRepository


class CategoriaService:
    def __init__(self):
        self.repository = CategoriaRepository()

    def get_all(self) -> list[Categoria]:
        return self.repository.get_all()
