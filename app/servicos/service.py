from django.http import JsonResponse
from app.servicos.models import Servicos
from app.servicos.schemas import  ServicoSchema
from app.utils.jwt_manager import authenticate

class ServicoService:
    def get_servico(self, empresa_id: str):
        return Servicos.objects.filter(empresa_id=empresa_id) 

    def create_servico(self, payload: ServicoSchema):
        if Servicos.objects.filter(servico=payload.servico, empresa_id=payload.empresa_id):
            return JsonResponse(data={'error': "Serviço já cadastrado"}, status=400) 
        servico = Servicos.objects.create(**payload.dict())
        return JsonResponse(data={"message": "CREATE", "sucess": f'{"Serviço criado com sucesso"} - {servico.id}'}, status=200)
    
    def delete_servico(self, servico_id: str):
        servico = Servicos.objects.filter(id=servico_id)
        servico.delete()
        return JsonResponse(data={"message": "DELETE", "sucess": "Serviço excluído com sucesso"}, status=200)
