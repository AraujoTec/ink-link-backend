from ninja import Router, Query
from app.authenticate.service import JWTAuth
from app.detalhe_servico.schemas import DetalheBase, DetalheSchemaOut, FiltersSchema
from app.detalhe_servico.service import DetalheService

detalhes_router = Router(auth=JWTAuth(), tags=["Detalhes do Serviço"])


#GETS
@detalhes_router.get("", response=list[DetalheSchemaOut])
def get_servico(request):
    service = DetalheService(request)
    return service.get_servico()   
 
@detalhes_router.get("reports/")
def create_csv(request, filters: FiltersSchema = Query(...)):
    service = DetalheService(request)
    return service.create_csv(filters)


#POST
@detalhes_router.post("detalhe")
def create_servico(request, payload: DetalheBase):
    service = DetalheService(request)
    return service.create_servico(payload)

#PATCH
@detalhes_router.patch("{detalhe_id}")
def update_servico(request, detalhe_id: str, payload: DetalheBase):
    service = DetalheService(request)
    return service.update_servico(detalhe_id, payload)

#DELETE
@detalhes_router.delete("{detalhe_id}")
def delete_servico(request, detalhe_id: str):
    service = DetalheService(request)
    return service.delete_servico(detalhe_id)

