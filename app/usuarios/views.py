from ninja import Router
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from app.usuarios.models import Usuarios
from app.usuarios.schemas import UserSchemaOut, UserSchemaIn
from app.usuarios.auth import AuthBearer, BasicAuth

router = Router()


@router.get("/", response=list[UserSchemaOut], auth=AuthBearer())
def get_user(request):
    return Usuarios.objects.all() 

@router.get("/{user_id}", response=UserSchemaOut, auth=BasicAuth())
def get_users_by_id(request, user_id: int):
    return get_object_or_404(Usuarios, pk=user_id)

@router.post("/")
def create_user(request, payload:UserSchemaIn):
    user = User.objects.create_user(**payload.dict)
    
    return 