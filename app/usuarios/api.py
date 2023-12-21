from ninja import Router
from django.http import JsonResponse
from app.usuarios.service import UsuariosService
from app.usuarios.schemas import UserSchemaOut, UserSchemaIn, SuperUser
from app.authenticate.service import JWTAuth
from app.utils.jwt_manager import authenticate

router = Router(auth=JWTAuth(), tags=['Usuarios'])
service = UsuariosService()

def busca_empresa(token):
    return service.get_user(empresa_id=token.get("empresa_id"))

#GETS
@router.get("", response=list[UserSchemaOut])
def get_user(request):
    token = authenticate(request)
    return busca_empresa(token)
    

@router.get("{usuario_id}", response=UserSchemaOut)
def get_user_by_id(request, usuario_id: str):
    token = authenticate(request)
    return service.get_user_by_id(request, usuario_id=token.get("usuario_id"))
    

#POSTS
@router.post("", auth=None)
def create_user(request, payload:UserSchemaIn):
    return service.create_user(payload)
    

#PATCH
@router.patch("{usuario_id}")
def update_user(request, usuario_id: str, payload: UserSchemaIn):
    token = authenticate(request)
    if not busca_empresa(token).get(id=token.get("usuario_id")):
        return JsonResponse(data={'error': "usuário inválido"}, status=400)
    return service.update_user(request, usuario_id, payload)
    
    
@router.patch("superuser/{usuario_id}")
def create_super_user(request, usuario_id: str, payload:SuperUser):
    token = authenticate(request)
    if not busca_empresa(token).get(id=token.get("usuario_id")) and token.get("is_superuser"): 
        return JsonResponse(data={'error': "usuário não autorizado"}, status=400)
    return service.create_super_user(usuario_id, payload)
    

#DELETE
@router.delete("soft_delete/{usuario_id}")
def soft_delete_user(request, usuario_id: str):
    token = authenticate(request)
    if not busca_empresa(token).get(id=token.get("usuario_id")) and token.get("is_superuser"): 
        return JsonResponse(data={'error': "usuário não autorizado"}, status=400)
    return service.soft_delete_user(request, usuario_id)
    

@router.delete("{usuario_id}")
def delete_user(request, usuario_id: str):
    token = authenticate(request)
    if not busca_empresa(token).get(id=token.get("usuario_id")) and token.get("is_superuser"): 
        return JsonResponse(data={'error': "usuário não autorizado"}, status=400)    
    return service.delete_user(request, usuario_id) 
    
   