from ninja import Router
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from app.usuarios.models import Usuarios
from app.usuarios.schemas import UserSchemaOut, UserSchemaIn, UserUpdate, UserSoftDelete, SuperUser
from app.auth import AuthBearer

 
router = Router()
_TGS = ['Usuarios']

#GETS
@router.get("/", tags=_TGS, response=list[UserSchemaOut])
def get_user(request):
    return Usuarios.objects.filter(deleted=False) 

@router.get("/{username}", tags=_TGS, response=UserSchemaOut)
def get_users_by_username(request, username: str):
    return get_object_or_404(Usuarios, username=username)

#POSTS
@router.post("/", tags=_TGS)
def create_user(request, payload:UserSchemaIn):
    busca_cpf = Usuarios.objects.filter(cpf=payload.cpf)
    if not busca_cpf :
        if payload.cpf.isdigit() == True: 
            user = Usuarios.objects.create_user(**payload.dict())
            return JsonResponse({"message": "CREATE", "sucess": f'{"Usuario cadastrado com sucesso"}-{user.uuid}'}, status=200)
        raise JsonResponse({'error': "CPF inválido"}, status=400)
    raise JsonResponse({'error': "CPF já cadastrado"}, status=400)

#PUTS
@router.put("/{username}", tags=_TGS)
def update_user(request, username: str, payload: UserUpdate):
    user = Usuarios.objects.filter(username=username, deleted=False).first()
    if not user:
        raise JsonResponse({'error': "Cadastro inativo"}, status=400)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(user, attr, value)
    user.save()
    return JsonResponse({"message": "UPDATE", "sucess": "Cadastro alterado com sucesso"}, status=200)
    

@router.put("/superuser/{username}", tags=_TGS, auth=AuthBearer())
def create_super_user(request, username: str, payload:SuperUser):
    user = get_object_or_404(Usuarios, username=username)
    for attr, value in payload.dict().items():
        setattr(user, attr, value)
    user.save()
    return JsonResponse({"message": "UPDATE", "sucess": "Permissão alterada com sucesso"}, status=200)

@router.put("/soft_delete/{username}", tags=_TGS)
def soft_delete_user(request, username: str, payload:UserSoftDelete):
    user = get_object_or_404(Usuarios, username=username)
    for attr, value in payload.dict().items():
        setattr(user, attr, value)
    user.save()
    if payload.is_active == False and payload.deleted == True:
        delete_user = Usuarios.objects.get(username=username)
        delete_user.soft_delete()
    return JsonResponse({"message": "DELETE", "sucess": "Usuario deletado com sucesso"}, status=200)

#DELETE
@router.delete("/{username}", tags=_TGS, auth=AuthBearer())
def delete_user(request, username: str):
    user = get_object_or_404(Usuarios, username=username)
    user.delete()
    return JsonResponse({"message": "DELETE", "sucess": "Usuario excluida com sucesso"}, status=200)

