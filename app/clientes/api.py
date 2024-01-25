from ninja import Router, Query
from app.authenticate.service import JWTAuth
from app.clientes.service import ClienteService
from app.clientes.schemas import ClienteSchemaIn, ClienteSchemaOut, FiltersSchema


clientes_router = Router(auth=JWTAuth(), tags=['Clientes'])


# GETS
@clientes_router.get("", response=list[ClienteSchemaOut])
def get_cliente(request):
    service = ClienteService (request)
    return service.get_cliente()
    
@clientes_router.get("{cliente_id}", response=list[ClienteSchemaOut])
def get_cliente_by_id(request, cliente_id: str):
    service = ClienteService (request)
    return service.get_cliente_by_id(cliente_id)
    
@clientes_router.get("reports/")
def create_csv(request, filters: FiltersSchema = Query(...)):
    service = ClienteService (request)
    return service.create_csv(filters)

#POSTS
@clientes_router.post("", auth=None, response=list[ClienteSchemaOut])
def create_cliente(request, payload:ClienteSchemaIn):
    service = ClienteService (request)
    return service.create_cliente(payload)
    

#PATCH
@clientes_router.patch("{cliente_id}", response=list[ClienteSchemaOut])
def update_cliente(request, cliente_id: str, payload: ClienteSchemaIn):
    service = ClienteService (request)
    return service.update_cliente(cliente_id, payload)
    

#DELETE
@clientes_router.delete("soft_delete/{cliente_id}")
def soft_delete_cliente(request, cliente_id: str):
    service = ClienteService (request)
    return service.soft_delete_cliente(cliente_id)
    

@clientes_router.delete("{cliente_id}")
def delete_cliente(request, cliente_id: str):
    service = ClienteService (request)
    return service.delete_cliente(cliente_id) 
    
   