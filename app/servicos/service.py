from django.http import JsonResponse
from app.servicos.models import Servicos
from app.servicos.schemas import  ServicoSchema
from app.utils.jwt_manager import authenticate

class ServicoService:
    def get_servico(self, empresa_id: str):
        return Servicos.objects.filter(empresa_id=empresa_id) 

    def create_servico(self, request, payload: ServicoSchema):
        token = authenticate(request)
        
        if Servicos.objects.filter(servico=payload.servico, empresa_id=token.get("empresa_id")):
            return JsonResponse(data={'error': "Serviço já cadastrado"}, status=400) 
        
        dados = payload.dict()
        dados["empresa_id"] = token.get("empresa_id")
        
        servico = Servicos.objects.create(**dados)
        return JsonResponse(data={"sucess": f'{"Serviço criado com sucesso"} - {servico.id}'}, status=200)
    
    def delete_servico(self, servico_id: str, empresa_id: str):
        servico = Servicos.objects.filter(id=servico_id, empresa_id=empresa_id)
        servico.delete()
        return JsonResponse(data={"sucess": "Serviço excluído com sucesso"}, status=200)
