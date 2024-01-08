from ninja import Router
from django.http import JsonResponse, FileResponse
from app.usuarios.service import UsuariosService
from app.usuarios.schemas import UserSchemaOut, UserSchemaIn
from app.authenticate.service import JWTAuth
from app.utils.jwt_manager import authenticate


colaborador_router = Router(auth=JWTAuth(), tags=['Colaborador'])
service = UsuariosService()

def busca_usuarios(token):
    return service.get_user(empresa_id=token.get("empresa_id"))

#GETS
@colaborador_router.get("", response=list[UserSchemaOut])
def get_user(request):
    token = authenticate(request)
    return busca_usuarios(token)
    
@colaborador_router.get("{usuario_id}", response=list[UserSchemaOut])
def get_user_by_id(request, usuario_id: str):
    token = authenticate(request)
    return service.get_user_by_id(request, usuario_id=token.get("usuario_id"))
    
@colaborador_router.get("relatorio/")
def create_csv(request):
    service.create_csv(request)
    return FileResponse(open("/home/gabriel/Documentos/projetos/ink-link-backend/app/utils/docs/relatorios.csv", 'rb'), as_attachment=True)


#POSTS
@colaborador_router.post("", auth=None)
def create_user(request, payload:UserSchemaIn):
    return service.create_user(payload)
    

#PATCH
@colaborador_router.patch("{usuario_id}")
def update_user(request, usuario_id: str, payload: UserSchemaIn):
    token = authenticate(request)
    if not busca_usuarios(token).get(id=token.get("usuario_id")):
        return JsonResponse(data={'error': "usuário inválido"}, status=400)
    return service.update_user(request, usuario_id, payload)
    
    
@colaborador_router.patch("superuser/{usuario_id}")
def create_super_user(request, usuario_id: str):
    token = authenticate(request)
    if not busca_usuarios(token).get(id=token.get("usuario_id")):
        return JsonResponse(data={'error': "usuário inválido"}, status=400)
    return service.create_super_user(request, usuario_id)
    

#DELETE
@colaborador_router.delete("soft_delete/{usuario_id}")
def soft_delete_user(request, usuario_id: str):
    token = authenticate(request)
    if not busca_usuarios(token).get(id=token.get("usuario_id")):
        return JsonResponse(data={'error': "usuário inválido"}, status=400)
    return service.soft_delete_user(request, usuario_id)
    

@colaborador_router.delete("{usuario_id}")
def delete_user(request, usuario_id: str):
    token = authenticate(request)    
    if not busca_usuarios(token).get(id=token.get("usuario_id")):
        return JsonResponse(data={'error': "usuário inválido"}, status=400)
    return service.delete_user(request, usuario_id) 
    
   