from app.models import Estado
from app.repositories import EstadoRepository


class EstadoService:
    def __init__(self):
        self.repository = EstadoRepository()

    def get_all(self) -> list[Estado]:
        return self.repository.get_all()