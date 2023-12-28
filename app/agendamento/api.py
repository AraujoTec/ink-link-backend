from ninja import Router
from django.http import FileResponse
from app.agendamento.service import AgendaService
from app.agendamento.schemas import AgendaSchemaOut, AgendaBase
from app.authenticate.service import JWTAuth
from app.utils.jwt_manager import authenticate

agendamento_router = Router(auth=JWTAuth(), tags=["Agendamento"])
service = AgendaService ()


#GETS
@agendamento_router.get("", response=list[AgendaSchemaOut])
def get_agenda(request):
    token = authenticate(request)
    return service.get_agenda(token.get("empresa_id"))    
    
@agendamento_router.get("{agendamento_id}", response=list[AgendaSchemaOut])
def get_agendamento_by_id(request, agendamento_id: str):
    token = authenticate(request)
    return service.get_agendamento_by_id(agendamento_id, token.get("empresa_id"))

@agendamento_router.get("colaborador/{colaborador_id}", response=list[AgendaSchemaOut])
def get_agenda_by_colaborador(request, colaborador_id: str):
    token = authenticate(request)
    return service.get_agenda_by_colaborador(colaborador_id, token.get("empresa_id"))

@agendamento_router.get("relatorio/")
def create_csv(request):
    service.create_csv(request)
    return FileResponse(open("/home/gabriel/Documentos/projetos/ink-link-backend/app/utils/docs/relatorios.csv", 'rb'), as_attachment=True)

#POST
@agendamento_router.post("")
def create_agenda(request, payload: AgendaBase):
    return service.create_agenda(request, payload)
    

#PATCH
@agendamento_router.patch("{agendamento_id}", response=list[AgendaSchemaOut])
def update_agenda(request, agendamento_id: str, payload: AgendaBase):
    token = authenticate(request)
    return service.update_agenda(agendamento_id, token.get("empresa_id"), payload)
    

#DELETE
@agendamento_router.delete("{agendamento_id}")
def delete_agenda(request, agendamento_id: str):
    token = authenticate(request)
    return service.delete_agenda(agendamento_id, token.get("empresa_id"))
    
