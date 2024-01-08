from django.http import JsonResponse
from app.agendamento.models import Agendamento
from app.agendamento.schemas import AgendaBase
from app.utils.jwt_manager import authenticate
import csv
class AgendaService:
    
    def get_agenda(self, empresa_id: str):
        return Agendamento.objects.filter(empresa_id=empresa_id) 

    def get_agendamento_by_id(self, agendamento_id: str, empresa_id: str):
        return Agendamento.objects.filter(id=agendamento_id, empresa_id=empresa_id)
    
    def get_agenda_by_colaborador(self, colaborador_id: str, empresa_id: str):
        return Agendamento.objects.filter(colaborador_id=colaborador_id, empresa_id=empresa_id)

    def create_csv(self, request):
        token = authenticate(request)
        agenda = self.get_agenda(token.get("empresa_id"))
        dados = [[
                    'agendamento_id',
                    'cliente',
                    'empresa',
                    'colaborador',
                    'detalhes_servico',
                    'data_agendamento',
                    'data_pagamento',
                    'forma_pagamento'],]
    
        for itens in agenda:
            valores = [
                str(itens.id),
                str(itens.cliente),
                str(itens.colaborador),
                str(itens.empresa),
                str(itens.detalhes_servico),
                str(itens.data_agendamento),
                str(itens.data_pagamento),
                str(itens.forma_pagamento)]
            dados.append(valores)
    
        with open('/home/gabriel/Documentos/projetos/ink-link-backend/app/utils/docs/relatorios.csv', 'w') as arquivo:
            relatorio_agenda = csv.writer(arquivo)
            for linha in dados:
                relatorio_agenda.writerow(linha)
        
        return JsonResponse(data={"sucess": "Relatório disponibilizado"}, status=200)
    
    
    def create_agenda(self, payload: AgendaBase):
        agendamento = Agendamento.objects.create(**payload.dict())
        return JsonResponse(data={"sucess": f'{"Agenda cadastrada com sucesso"} - {agendamento.id}'}, status=200)
    
    def update_agenda(self, agendamento_id: str, empresa_id: str, payload: AgendaBase):
        agenda = self.get_agendamento_by_id(agendamento_id=agendamento_id, empresa_id=empresa_id)
        for attr, value in payload.dict().items():
            setattr(agenda, attr, value)
        agenda.save()
        return JsonResponse(data={"sucess": "Agenda alterada com sucesso"}, status=200)

    def delete_agenda(self, agendamento_id: str, empresa_id: str):
        agenda = self.get_agendamento_by_id(agendamento_id=agendamento_id, empresa_id=empresa_id)
        agenda.delete()
        return JsonResponse(data={"sucess": "Empresa excluida com sucesso"}, status=200)
