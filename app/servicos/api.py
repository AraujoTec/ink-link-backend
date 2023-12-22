from ninja import Router
from app.servicos.service import ServicoService
from app.servicos.schemas import ServicoSchema, ServicoSchemaOut
from app.authenticate.service import JWTAuth
from app.utils.jwt_manager import authenticate

servicos_router = Router(tags=['Serviços'])
service = ServicoService ()

#GETS
@servicos_router.get("{empresa_id}", response=list[ServicoSchemaOut])
def get_servico(request, empresa_id: str):
    response = service.get_servico(empresa_id)    
    return response

#POST
@servicos_router.post("servico")
def create_servico(request, payload: ServicoSchema):
    response = service.create_servico(payload)
    return response

#DELETE
@servicos_router.delete("{servico_id}")
def delete_servico(servico_id: str):
    response = service.delete_servico(servico_id)
    return response

