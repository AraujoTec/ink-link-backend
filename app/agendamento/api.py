from ninja import Router, Query
from app.agendamento.service import AgendaService
from app.agendamento.schemas import AgendaSchemaOut, AgendaBase, FiltersSchema
from app.authenticate.service import JWTAuth

agendamento_router = Router(auth=JWTAuth(), tags=["Agendamento"])

#GETS
@agendamento_router.get("", response=list[AgendaSchemaOut])
def get_agenda(request):
    service = AgendaService(request)
    return service.get_agenda()    
    
@agendamento_router.get("{agendamento_id}", response=list[AgendaSchemaOut])
def get_agendamento_by_id(request, agendamento_id: str):
    service = AgendaService(request)
    return service.get_agendamento_by_id(agendamento_id)

@agendamento_router.get("colaborador/{colaborador_id}", response=list[AgendaSchemaOut])
def get_agenda_by_colaborador(request, colaborador_id: str):
    service = AgendaService(request)
    return service.get_agenda_by_colaborador(colaborador_id)

@agendamento_router.get("reports/")
def create_csv(request, filters: FiltersSchema = Query(...)):
    service = AgendaService(request)
    return service.create_csv(filters)
    

#POST
@agendamento_router.post("")
def create_agenda(request, payload: AgendaBase):
    service = AgendaService(request)
    return service.create_agenda(payload)
    

#PATCH
@agendamento_router.patch("{agendamento_id}", response=list[AgendaSchemaOut])
def update_agenda(request, agendamento_id: str, payload: AgendaBase):
    service = AgendaService(request)
    return service.update_agenda(agendamento_id, payload)
    

#DELETE
@agendamento_router.delete("{agendamento_id}")
def delete_agenda(request, agendamento_id: str):
    service = AgendaService(request)
    return service.delete_agenda(agendamento_id)
    
