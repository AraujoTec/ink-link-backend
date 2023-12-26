from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from app.agendamento.models import Agendamento
from app.agendamento.schemas import AgendaBase

class AgendaService:
    
    def _get_empresa_by_cnpj(self, cnpj):
        return Agendamento.objects.filter(cnpj=cnpj, deleted=False)
    
    def get_agenda(self):
        return Agendamento.objects.all() 

    def get_agendamento_by_id(self,agendamento_id: str):
        return get_object_or_404(Agendamento, id=agendamento_id)

    def create_agenda(self, payload: AgendaBase):
        agendamento = Agendamento.objects.create(**payload.dict())
        return JsonResponse(data={"message": "CREATE", "sucess": f'{"Agenda cadastrada com sucesso"} - {agendamento.id}'}, status=200)
    
    def update_agenda(self, agendamento_id: str, payload: AgendaBase):
        agenda = self.get_agendamento_by_id(agendamento_id=agendamento_id)
        for attr, value in payload.dict.items():
            setattr(agenda, attr, value)
        agenda.save()
        return JsonResponse(data={"message": "UPDATE", "sucess": "Agenda alterada com sucesso"}, status=200)

    def delete_agenda(self, agendamento_id: str):
        agenda = Agendamento.objects.get(agendamento_id=agendamento_id)
        agenda.delete()
        return JsonResponse(data={"message": "DELETE", "sucess": "Empresa excluida com sucesso"}, status=200)
