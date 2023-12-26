from ninja import Router
from app.agendamento.service import AgendaService
from app.agendamento.schemas import AgendaSchemaOut, AgendaBase
from app.authenticate.service import JWTAuth
from app.utils.jwt_manager import authenticate
from django.http import JsonResponse

agendamento_router = Router()
service = AgendaService ()

#GETS
@agendamento_router.get("", response=list[AgendaSchemaOut])
def get_agenda(request):
    return service.get_agenda()    
    

@agendamento_router.get("{agendamento_id}", response=AgendaSchemaOut)
def get_agendamento_by_id(request, agendamento_id: str):
    return service.get_agendamentos_by_id(id = agendamento_id)

#POST
@agendamento_router.post("")
def create_agenda(request, payload: AgendaBase):
    return service.create_agenda(request, payload)
    

#PATCH
@agendamento_router.patch("{agendamento_id}")
def update_agenda(request, agendamento_id: str, payload: AgendaBase):
    return service.update_agenda(agendamento_id, payload)
    

#DELETE
@agendamento_router.delete("{agendamento_id}")
def delete_agenda(request, agendamento_id: str):
    return service.delete_agenda(agendamento_id)
    
