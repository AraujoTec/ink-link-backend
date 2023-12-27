from ninja import Router
from app.authenticate.service import JWTAuth
from app.clientes.service import ClienteService
from app.clientes.schemas import ClienteSchemaIn, ClienteSchemaOut
from app.utils.jwt_manager import authenticate

clientes_router = Router(auth=JWTAuth(), tags=['Clientes'])
service = ClienteService ()

# GETS
@clientes_router.get("", response=list[ClienteSchemaOut])
def get_cliente(request):
    token = authenticate(request)
    return service.get_cliente(token.get("empresa_id"))
    
@clientes_router.get("{cliente_id}", response=list[ClienteSchemaOut])
def get_cliente_by_id(request, cliente_id: str):
    token = authenticate(request)
    return service.get_cliente_by_id(cliente_id, token.get("empresa_id"))
    

#POSTS
@clientes_router.post("", auth=None, response=list[ClienteSchemaOut])
def create_cliente(request, payload:ClienteSchemaIn):
    return service.create_cliente(payload)
    

#PATCH
@clientes_router.patch("{cliente_id}", response=list[ClienteSchemaOut])
def update_cliente(request, cliente_id: str, payload: ClienteSchemaIn):
    token = authenticate(request)
    return service.update_cliente(cliente_id, token.get("empresa_id"), payload)
    

#DELETE
@clientes_router.delete("soft_delete/{cliente_id}")
def soft_delete_cliente(request, cliente_id: str):
    token = authenticate(request)
    return service.soft_delete_cliente(cliente_id, token.get("empresa_id"))
    

@clientes_router.delete("{cliente_id}")
def delete_cliente(request, cliente_id: str):
    token = authenticate(request)
    return service.delete_cliente(cliente_id, token.get("empresa_id")) 
    
   