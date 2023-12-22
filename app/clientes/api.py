from ninja import Router
from app.clientes.service import ClienteService
from app.clientes.schemas import ClienteSchemaIn, ClienteSchemaOut


clientes_router = Router(tags=['Clientes'])
service = ClienteService ()

# GETS
@clientes_router.get("{cliente_id}", response=ClienteSchemaOut)
def get_cliente_by_id(request, cliente_id: str):
    return service.get_cliente_by_id(cliente_id=cliente_id)
    

#POSTS
@clientes_router.post("", auth=None)
def create_cliente(request, payload:ClienteSchemaIn):
    return service.create_cliente(payload)
    

#PATCH
@clientes_router.patch("{cliente_id}")
def update_cliente(request, cliente_id: str, payload: ClienteSchemaIn):
    return service.update_cliente(cliente_id, payload)
    

#DELETE
@clientes_router.delete("soft_delete/{cliente_id}")
def soft_delete_cliente(request, cliente_id: str):
    return service.soft_delete_cliente(request, cliente_id)
    

@clientes_router.delete("{cliente_id}")
def delete_cliente(request, cliente_id: str):
    return service.delete_cliente(cliente_id) 
    
   