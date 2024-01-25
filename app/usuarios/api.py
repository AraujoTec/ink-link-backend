from ninja import Router, Query
from django.http import JsonResponse
from app.usuarios.service import UsuariosService
from app.usuarios.schemas import UserSchemaOut, UserSchemaIn, FiltersSchema
from app.authenticate.service import JWTAuth

colaborador_router = Router(auth=JWTAuth(), tags=['Colaborador'])


def busca_usuarios(request):
    service = UsuariosService(request)
    return service.get_user()

#GETS
@colaborador_router.get("", response=list[UserSchemaOut])
def get_user(request):
    return busca_usuarios(request)
    
@colaborador_router.get("{usuario_id}", response=list[UserSchemaOut])
def get_user_by_id(request, usuario_id: str):
    service = UsuariosService(request)
    return service.get_user_by_id(usuario_id)
    
@colaborador_router.get("reports/")
def create_csv(request, filters: FiltersSchema = Query(...)):
    service = UsuariosService(request)
    return service.create_csv(filters)
    

#POSTS
@colaborador_router.post("", auth=None)
def create_user(request, payload:UserSchemaIn):
    service = UsuariosService(request)
    return service.create_user(payload)
    

#PATCH
@colaborador_router.patch("{usuario_id}")
def update_user(request, usuario_id: str, payload: UserSchemaIn):
    service = UsuariosService(request)
    if not busca_usuarios():
        return JsonResponse(data={'error': "usuário inválido"}, status=400)
    return service.update_user(usuario_id, payload)
    
    
@colaborador_router.patch("superuser/{usuario_id}")
def create_super_user(request, usuario_id: str):
    service = UsuariosService(request)
    if not busca_usuarios():
        return JsonResponse(data={'error': "usuário inválido"}, status=400)
    return service.create_super_user(usuario_id)
    

#DELETE
@colaborador_router.delete("soft_delete/{usuario_id}")
def soft_delete_user(request, usuario_id: str):
    service = UsuariosService(request)
    if not busca_usuarios():
        return JsonResponse(data={'error': "usuário inválido"}, status=400)
    return service.soft_delete_user(usuario_id)
    

@colaborador_router.delete("{usuario_id}")
def delete_user(request, usuario_id: str):
    service = UsuariosService(request)    
    if not busca_usuarios():
        return JsonResponse(data={'error': "usuário inválido"}, status=400)
    return service.delete_user(usuario_id) 
    
   