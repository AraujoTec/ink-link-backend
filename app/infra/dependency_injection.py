from typing import Optional

from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import Depends
from app.infra.database import get_db
from app.repository import UsuariosRepository
from app.models import Usuarios
from app.services import UsuariosService

def get_usuario_repository(db: Session = Depends(get_db)):
    return UsuariosRepository(db)

def get_usuario_service(usuario_repository: UsuariosRepository = Depends(get_usuario_repository)):
    return UsuariosService(usuario_repository)