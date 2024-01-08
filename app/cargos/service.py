from django.http import JsonResponse
from app.cargos.models import Cargos
from app.cargos.schemas import  CargoSchema
from app.utils.jwt_manager import authenticate

class CargosService:
    def get_cargo(self, empresa_id: str):
        return Cargos.objects.filter(empresa_id=empresa_id) 

    def create_cargo(self,request, payload: CargoSchema):
        token = authenticate(request)
                
        if Cargos.objects.filter(cargo=payload.cargo, empresa_id=token.get("empresa_id")):
            return JsonResponse(data={'error': "Cargo já cadastrado"}, status=400) 
        
        
        dados = payload.dict()
        dados["empresa_id"] = token.get("empresa_id")
        
        cargo = Cargos.objects.create(**dados)
        return JsonResponse(data={"sucess": f'{"Cargo criado com sucesso"} - {cargo.id}'}, status=200)
    
    def delete_cargo(self, request, cargo_id: str):
        token = authenticate(request)
        cargo = Cargos.objects.filter(id=cargo_id, empresa_id=token.get("empresa_id"))
        cargo.delete()
        return JsonResponse(data={"sucess": "Cargo excluido com sucesso"}, status=200)
