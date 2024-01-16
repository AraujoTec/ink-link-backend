from ninja import Router, Query
from django.http import JsonResponse
from app.materiais.service import MateriaisService
from app.materiais.schemas import MateriaisSchema, MateriaisSchemaOut, FiltersSchema
from app.authenticate.service import JWTAuth
from app.utils.jwt_manager import authenticate


materiais_router = Router(auth=JWTAuth(), tags=["Materiais"] )

#GETS
@materiais_router.get("", response=list[MateriaisSchemaOut])
def get_itens(request):
    service = MateriaisService(request)
    return service.get_itens(request)
    
@materiais_router.get("{item_id}", response=list[MateriaisSchemaOut])
def get_item_by_id(request, item_id: int):
    service = MateriaisService(request)
    return service.get_item_by_id(request, item_id)
    
@materiais_router.get("relatorios/")
def create_csv(request, filters: FiltersSchema = Query(...)):
    service = MateriaisService(request)
    return service.create_csv(request, filters)

#POSTS
@materiais_router.post("")
def create_item(request, payload:MateriaisSchema):
    service = MateriaisService(request)
    return service.create_item(request, payload)
    

#PUTS
@materiais_router.put("{item_id}")
def update_item(request, item_id: str, payload: MateriaisSchema):
    service = MateriaisService(request)
    return service.update_item(request, item_id, payload)
    
#DELETE
@materiais_router.delete("{item_id}")
def delete_item(request, item_id: int):
    service = MateriaisService(request)
    return service.delete_item(request, item_id)
    
