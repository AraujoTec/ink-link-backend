from ninja import Router
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from app.usuarios.models import Usuarios
from app.usuarios.schemas import UserSchemaOut, UserSchemaIn, UserUpdate, UserSoftDelete, SuperUser
from app.auth import AuthBearer

router = Router()
_TGS = ['CRUD Usuarios']

#GETS
@router.get("/", tags=_TGS, response=list[UserSchemaOut])
def get_user(request):
    return Usuarios.objects.filter(deleted=False) 

@router.get("/{username}", tags=_TGS, response=UserSchemaOut)
def get_users_by_id(request, username: str):
    return get_object_or_404(Usuarios, username=username)

#POSTS
@router.post("/", tags=_TGS)
def create_user(request, payload:UserSchemaIn):
    busca_cpf = Usuarios.objects.filter(cpf=payload.cpf)
    if not busca_cpf :
        if payload.cpf.isdigit() == True: 
            user = Usuarios.objects.create_user(**payload.dict())
            return 200, {"message": "CREATE", "sucess": f'{"Usuário cadastrado com sucesso"}-{user.uuid}'}
        raise HttpError(400, "CPF inválido")
    raise HttpError(400, "CPF já cadastrado")

#PUTS
@router.put("/{username}", tags=_TGS)
def update_user(request, username: str, payload: UserUpdate):
    user = get_object_or_404(Usuarios, username=username)
    lista_users = list(Usuarios.objects.filter(deleted=False))
    if user in lista_users:
        for attr, value in payload.dict(exclude_unset=True).items():
            setattr(user, attr, value)
        user.save()
        return 200, {"message": "UPDATE", "sucess": "Usuário alterado com sucesso" }
    raise HttpError(404, "Usuário inativo")

@router.put("/superuser/{username}", tags=_TGS, auth=AuthBearer())
def create_super_user(request, username: str, payload:SuperUser):
    user = get_object_or_404(Usuarios, username=username)
    for attr, value in payload.dict().items():
        setattr(user, attr, value)
    user.save()
    return 200, {"message": "CREATE SUPER_USER", "sucess": "Usuário alterado com sucesso"}

@router.put("/soft_delete/{username}", tags=_TGS)
def soft_delete_user(request, username: str, payload:UserSoftDelete):
    user = get_object_or_404(Usuarios, username=username)
    for attr, value in payload.dict().items():
        setattr(user, attr, value)
    user.save()
    if payload.is_active == False and payload.deleted == True:
        delete_user = Usuarios.objects.get(username=username)
        delete_user.soft_delete()
    return 200, {"message": "DELETE", "sucess": "Usuário deletado com sucesso"}

#DELETE
@router.delete("/{username}", tags=_TGS, auth=AuthBearer())
def delete_user(request, username: str):
    user = get_object_or_404(Usuarios, username=username)
    user.delete()
    return 200, {"message": "DELETE", "sucess": "Usuário deletado com sucesso"}


