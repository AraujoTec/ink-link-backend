from ninja import Router
from app.materiais.service import MateriaisService
from app.materiais.schemas import MateriaisSchema
from app.authenticate.service import JWTAuth
from app.utils.jwt_manager import authenticate
from django.http import JsonResponse

materiais_router = Router(auth=JWTAuth(), tags=["Materiais"] )

service = MateriaisService()

#GETS
@materiais_router.get("/", response=list[MateriaisSchema])
def get_itens(request):
    token = authenticate(request)
    response = service.get_itens(request, empresa_id=token.get("empresa_id"))
    return response

@materiais_router.get("/{item_id}", response=MateriaisSchema)
def get_item_by_id(request, item_id: int):
    token = authenticate(request)
    response = service.get_item_by_id(request, item_id, empresa_id=token.get("empresa_id"))
    return response

#POSTS
@materiais_router.post("/")
def create_item(request, payload:MateriaisSchema):
    token = authenticate(request)
    if not token.get["empresa_id"] == payload.empresa_id:
        return JsonResponse(data={'error': "usuário inválido"}, status=400)
    response = service.create_item(payload)
    return response

#PUTS
@materiais_router.put("/{item_id}")
def update_item(request, item_id: str, payload: MateriaisSchema):
    token = authenticate(request)
    if not token.get["empresa_id"] == payload.empresa_id:
        return JsonResponse(data={'error': "usuário inválido"}, status=400)
    response = service.update_item(item_id, payload)
    return response

#DELETE
@materiais_router.delete("/{item_id}")
def delete_item(request, item_id: int):
    token = authenticate(request)
    if not token.get["empresa_id"]:
        return JsonResponse(data={'error': "usuário inválido"}, status=400)
    response = service.delete_item(item_id)
    return response
