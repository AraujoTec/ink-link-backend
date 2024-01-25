from django.http import JsonResponse
from app.cargos.models import Cargos
from app.cargos.schemas import  CargoSchema
from app.utils.jwt_manager import authenticate

class CargosService:
    
    def __init__(self, request):
        self.token = authenticate(request)
        self.empresa = self.token.get("empresa_id")
    
    def get_cargo(self):
        return Cargos.objects.filter(empresa_id=self.empresa) 

    def create_cargo(self, payload: CargoSchema):
              
        if Cargos.objects.filter(cargo=payload.cargo, empresa_id=self.empresa):
            return JsonResponse(data={'error': "Cargo já cadastrado"}, status=400) 
        
        
        dados = payload.dict()
        dados["empresa_id"] = self.empresa
        
        cargo = Cargos.objects.create(**dados)
        return JsonResponse(data={"sucess": f'{"Cargo criado com sucesso"} - {cargo.id}'}, status=200)
    
    def delete_cargo(self, cargo_id: str):
        cargo = Cargos.objects.filter(id=cargo_id, empresa_id=self.empresa)
        cargo.delete()
        return JsonResponse(data={"sucess": "Cargo excluido com sucesso"}, status=200)
