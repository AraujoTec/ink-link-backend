
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from app.empresas.models import Empresas
from app.empresas.schemas import EmpresaSchemaIn
from app.utils.busca_cnpj import busca_cnpj
from app.utils.jwt_manager import authenticate

class EmpresasService:
    
    def _get_empresa_by_cnpj(self, cnpj):
        return Empresas.objects.filter(cnpj=cnpj, deleted=False)
    
    def get_empresa(self):
        return Empresas.objects.filter(deleted=False) 

    def get_empresas_by_cnpj(self,cnpj: str):
        return get_object_or_404(Empresas, cnpj=cnpj)


    def get_empresas_by_id(self,empresa_id: str):
        return get_object_or_404(Empresas, id=empresa_id)
    
    def autocomplete_empresa(self, request, cnpj: str):
        dados_cadastrais = busca_cnpj(cnpj=cnpj)
        if not dados_cadastrais:
            return JsonResponse(data={'error': "CNPJ inválido"}, status=400) 
        token = authenticate(request) 
        return {
            'razao_social': dados_cadastrais["nome"],
            'nome_fantasia': dados_cadastrais["fantasia"],
            'cnpj':cnpj,
            'telefone': dados_cadastrais["telefone"],
            'user_criacao': token.get("usuario_id"),
            }   

    def create_empresa(self, request, payload: EmpresaSchemaIn):
        
        if not payload.cnpj.isdigit():
            return JsonResponse(data={'error': "CNPJ inválido"}, status=400) 
        
        if self._get_empresa_by_cnpj(payload.cnpj).exists():
            return JsonResponse(data={'error': "CNPJ já cadastrado"}, status=400) 
        
        empresa = Empresas.objects.create(**payload.dict())
        return JsonResponse(data={"message": "CREATE", "sucess": f'{"Empresa cadastrada com sucesso"} - {empresa.id}'}, status=200)
    
    def update_empresa(self, request, empresa_id: str, payload: EmpresaSchemaIn):
        empresa = self.get_empresas_by_id(empresa_id=empresa_id)
        if not empresa:
            return JsonResponse(data={'error': "Cadatro inativo"}, status=400)
        
        token = authenticate(request)
        payload_dict = payload.dict()
        payload_dict["data_atualizacao"] = datetime.now()
        payload_dict["user_alteracao"] = token.get("usuario_id")    
                   
        for attr, value in payload_dict.items():
            setattr(empresa, attr, value)
        empresa.save()
        return JsonResponse(data={"message": "UPDATE", "sucess": "Empresa alterada com sucesso"}, status=200)

    def soft_delete_empresa(self, empresa_id: str):
        delete_empresa = Empresas.objects.get(id=empresa_id)
        delete_empresa.soft_delete()
        return JsonResponse(data={"message": "DELETE", "sucess": "Empresa deletada com sucesso"}, status=200)

    def delete_empresa(self, empresa_id: str):
        empresa = Empresas.objects.get(id=empresa_id)
        empresa.delete()
        return JsonResponse(data={"message": "DELETE", "sucess": "Empresa excluida com sucesso"}, status=200)