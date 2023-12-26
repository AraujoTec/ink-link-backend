from ninja import Router
from app.detalhe_servico.schemas import DetalheBase, DetalheSchemaOut
from app.detalhe_servico.service import DetalheService

detalhes_router = Router()

service = DetalheService ()

#GETS
@detalhes_router.get("", response=list[DetalheSchemaOut])
def get_servico(request):
    return service.get_servico()    

#POST
@detalhes_router.post("detalhe")
def create_servico(request, payload: DetalheBase):
    return service.create_servico(payload)

#PATCH
@detalhes_router.patch("{detalhe_id}")
def update_servico(request, detalhe_id: str, payload: DetalheBase):
    return service.update_servico(detalhe_id, payload)

#DELETE
@detalhes_router.delete("{detalhe_id}")
def delete_servico(detalhe_id: str):
    return service.delete_servico(detalhe_id)

