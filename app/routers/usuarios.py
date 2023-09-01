from fastapi import APIRouter, Depends
from datetime import datetime
from app.services import UsuariosService
from app.infra.dependency_injection import get_usuario_service

router = APIRouter()

@router.get('/')
async def get_all_users(
        usuario_service: UsuariosService = Depends(get_usuario_service),
):
    result = await usuario_service.get_all_users()
    return str(datetime.now())