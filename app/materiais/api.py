from ninja import Router
from app.materiais.service import MateriaisService
from app.materiais.schemas import MateriaisSchema
from app.authenticate.service import JWTAuth
from app.utils.jwt_manager import authenticate

router = Router(auth=JWTAuth(), tags=["Materiais"] )


service = MateriaisService()
#GETS
@router.get("/", response=list[MateriaisSchema])
def get_itens(request):
    token = authenticate(request)
    response = service.get_itens(empresa_id=token.get("empresa_id"))
    return response

@router.get("/{item_id}", response=MateriaisSchema)
def get_item_by_id(request, item_id: int):
    response = service.get_item_by_id(item_id)
    return response

#POSTS
@router.post("/")
def create_item(request, payload:MateriaisSchema):
    response = service.create_item(payload)
    return response

#PUTS
@router.put("/{item_id}")
def update_item(request, item_id: str, payload: MateriaisSchema):
    response = service.update_item(item_id, payload)
    return response

#DELETE
@router.delete("/{item_id}")
def delete_item(request, item_id: int):
    response = service.delete_item(item_id)
    return response
