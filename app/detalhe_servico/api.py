from ninja import Router
from app.authenticate.service import JWTAuth
from app.detalhe_servico.schemas import DetalheBase, DetalheSchemaOut
from app.detalhe_servico.service import DetalheService
from app.utils.jwt_manager import authenticate

detalhes_router = Router(auth=JWTAuth(), tags=["Detalhes do Serviço"])
service = DetalheService ()

#GETS
@detalhes_router.get("", response=list[DetalheSchemaOut])
def get_servico(request):
    token = authenticate(request)
    return service.get_servico(token.get("empresa_id"))    

#POST
@detalhes_router.post("detalhe")
def create_servico(request, payload: DetalheBase):
    return service.create_servico(payload)

#PATCH
@detalhes_router.patch("{detalhe_id}")
def update_servico(request, detalhe_id: str, payload: DetalheBase):
    token = authenticate(request)
    return service.update_servico(detalhe_id, token.get("empresa_id"), payload)

#DELETE
@detalhes_router.delete("{detalhe_id}")
def delete_servico(request, detalhe_id: str):
    token = authenticate(request)
    return service.delete_servico(detalhe_id, token.get("empresa_id"))

