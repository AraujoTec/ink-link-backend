from django.http import JsonResponse, FileResponse
from datetime import datetime
from app.settings import MEDIA_ROOT
from app.agendamento.models import Agendamento
from app.agendamento.schemas import AgendaBase
from app.utils.jwt_manager import authenticate
from app.utils.csv import format_csv, generate_csv

class AgendaService:
    def __init__(self, request):
        self.token = authenticate(request)
        self.empresa = self.token.get('empresa_id')
        self.agenda = Agendamento.objects.filter(empresa_id=self.empresa)

    def get_agenda(self):
        return self.agenda

    def get_agendamento_by_id(self, agendamento_id: str):
        return Agendamento.objects.filter(id=agendamento_id, empresa_id=self.empresa)
    
    def get_agenda_by_colaborador(self, colaborador_id: str):
        return Agendamento.objects.filter(colaborador_id=colaborador_id, empresa_id=self.empresa)

    def create_csv(self, filters):
        datetime_now = datetime.now()  
        path = f'{MEDIA_ROOT}/{self.empresa}'
        agenda = filters.filter(self.agenda)
        dados = format_csv(Agendamento)

        for itens in agenda:
            valores = [
                str(itens.id),
                str(itens.cliente),
                str(itens.empresa),
                str(itens.colaborador),
                str(itens.detalhes_servico),
                str(itens.data_agendamento),
                str(itens.data_pagamento),
                str(itens.forma_pagamento)]

            dados.append(valores)

        generate_csv(path, datetime_now, dados)

        return FileResponse(open(f'{path}/reports_{datetime_now}.csv', 'rb'), as_attachment=True)
    
    def create_agenda(self, payload: AgendaBase):
        agendamento = Agendamento.objects.create(**payload.dict())
        return JsonResponse(data={"sucess": f'{"Agenda cadastrada com sucesso"} - {agendamento.id}'}, status=200)
    
    def update_agenda(self, agendamento_id: str, payload: AgendaBase):
        agenda = self.get_agendamento_by_id(agendamento_id)
        for attr, value in payload.dict().items():
            setattr(agenda, attr, value)
        agenda.save()
        return JsonResponse(data={"sucess": "Agenda alterada com sucesso"}, status=200)

    def delete_agenda(self, agendamento_id: str):
        agenda = self.get_agendamento_by_id(agendamento_id)
        agenda.delete()
        return JsonResponse(data={"sucess": "Empresa excluida com sucesso"}, status=200)
