from django.http import JsonResponse
from app.servicos.models import Servicos
from app.servicos.schemas import  ServicoSchema
from app.utils.jwt_manager import authenticate

class ServicoService:
    
    def __init__(self, request):
        self.token = authenticate(request)
        self.empresa = self.token.get("empresa_id")
    
    
    def get_servico(self):
        return Servicos.objects.filter(empresa_id=self.empresa) 

    def create_servico(self, payload: ServicoSchema):
        
        if Servicos.objects.filter(servico=payload.servico, empresa_id=self.empresa):
            return JsonResponse(data={'error': "Serviço já cadastrado"}, status=400) 
        
        dados = payload.dict()
        dados["empresa_id"] = self.empresa
        
        servico = Servicos.objects.create(**dados)
        return JsonResponse(data={"sucess": f'{"Serviço criado com sucesso"} - {servico.id}'}, status=200)
    
    def delete_servico(self, servico_id: str):
        servico = Servicos.objects.filter(id=servico_id, empresa_id=self.empresa)
        servico.delete()
        return JsonResponse(data={"sucess": "Serviço excluído com sucesso"}, status=200)
