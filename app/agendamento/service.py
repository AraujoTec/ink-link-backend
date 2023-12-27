from django.http import JsonResponse
from app.agendamento.models import Agendamento
from app.agendamento.schemas import AgendaBase

class AgendaService:
    
    def get_agenda(self, empresa_id: str):
        return Agendamento.objects.filter(empresa_id=empresa_id) 

    def get_agendamento_by_id(self, agendamento_id: str, empresa_id: str):
        return Agendamento.objects.filter(id=agendamento_id, empresa_id=empresa_id)
    
    def get_agenda_by_colaborador(self, colaborador_id: str, empresa_id: str):
        return Agendamento.objects.filter(colaborador_id=colaborador_id, empresa_id=empresa_id)


    def create_agenda(self, payload: AgendaBase):
        agendamento = Agendamento.objects.create(**payload.dict())
        return JsonResponse(data={"sucess": f'{"Agenda cadastrada com sucesso"} - {agendamento.id}'}, status=200)
    
    def update_agenda(self, agendamento_id: str, empresa_id: str, payload: AgendaBase):
        agenda = self.get_agendamento_by_id(agendamento_id=agendamento_id, empresa_id=empresa_id)
        for attr, value in payload.dict.items():
            setattr(agenda, attr, value)
        agenda.save()
        return JsonResponse(data={"sucess": "Agenda alterada com sucesso"}, status=200)

    def delete_agenda(self, agendamento_id: str, empresa_id: str):
        agenda = self.get_agendamento_by_id(agendamento_id=agendamento_id, empresa_id=empresa_id)
        agenda.delete()
        return JsonResponse(data={"sucess": "Empresa excluida com sucesso"}, status=200)
