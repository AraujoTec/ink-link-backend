from ninja import Router
from django.http import JsonResponse, FileResponse
from app.materiais.service import MateriaisService
from app.materiais.schemas import MateriaisSchema
from app.authenticate.service import JWTAuth
from app.utils.jwt_manager import authenticate

materiais_router = Router(auth=JWTAuth(), tags=["Materiais"] )
service = MateriaisService()

#GETS
@materiais_router.get("", response=list[MateriaisSchema])
def get_itens(request):
    token = authenticate(request)
    return service.get_itens(token.get("empresa_id"))
    
@materiais_router.get("{item_id}", response=list[MateriaisSchema])
def get_item_by_id(request, item_id: int):
    token = authenticate(request)
    return service.get_item_by_id(item_id, token.get("empresa_id"))
    
@materiais_router.get("relatorios/")
def create_csv(request):
    service.create_csv(request)
    return FileResponse(open("/home/gabriel/Documentos/projetos/ink-link-backend/app/utils/docs/relatorios.csv", 'rb'), as_attachment=True)


#POSTS
@materiais_router.post("")
def create_item(request, payload:MateriaisSchema):
    token = authenticate(request)
    if not token.get("empresa_id") == str(payload.empresa_id):
        return JsonResponse(data={'error': "usuário inválido"}, status=400)
    return service.create_item(payload)
    

#PUTS
@materiais_router.put("{item_id}")
def update_item(request, item_id: str, payload: MateriaisSchema):
    token = authenticate(request)
    if not token.get("empresa_id") == str(payload.empresa_id):
        return JsonResponse(data={'error': "usuário inválido"}, status=400)
    return service.update_item(item_id, payload)
    

#DELETE
@materiais_router.delete("{item_id}")
def delete_item(request, item_id: int):
    token = authenticate(request)
    if not token.get("empresa_id"):
        return JsonResponse(data={'error': "usuário inválido"}, status=400)
    return service.delete_item(item_id)
    
