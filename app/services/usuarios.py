from app.repository import UsuariosRepository
from app.models import Usuarios


class UsuariosService:
    def __init__(self, usuarios_repository: UsuariosRepository) -> None:
        self.usuarios_repository = usuarios_repository


    async def get_all_users(self) -> Usuarios:
        resultado = self.usuarios_repository.get_all_users()
        return resultado