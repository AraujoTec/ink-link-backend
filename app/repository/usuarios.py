from sqlalchemy.orm import Session
from app.models import Usuarios
# from app.repository.base_repository import BaseRepository

class UsuariosRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_users(self):
        return self.db.query(Usuarios).all()
