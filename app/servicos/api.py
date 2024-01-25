from ninja import Router
from app.servicos.service import ServicoService
from app.servicos.schemas import ServicoSchema, ServicoSchemaOut
from app.authenticate.service import JWTAuth
from app.utils.jwt_manager import authenticate

servicos_router = Router(auth=JWTAuth(), tags=['Serviços'])

#GETS
@servicos_router.get("", response=list[ServicoSchemaOut])
def get_servico(request):
    service = ServicoService(request)
    return service.get_servico()    

#POST
@servicos_router.post("servico/")
def create_servico(request, payload: ServicoSchema):
    service = ServicoService(request)
    return service.create_servico(request, payload)
    

#DELETE
@servicos_router.delete("{servico_id}")
def delete_servico(request, servico_id: str):
    service = ServicoService(request)
    return service.delete_servico(servico_id)
    

