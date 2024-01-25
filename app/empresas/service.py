from datetime import datetime
from django.http import JsonResponse, FileResponse
from app.settings import MEDIA_ROOT
from app.empresas.models import Empresas
from app.empresas.schemas import EmpresaSchemaIn
from app.utils.busca_cnpj import busca_cnpj
from app.utils.jwt_manager import authenticate
from app.utils.csv import generate_csv, format_csv
class EmpresasService:
    
    def __init__(self, request):
        self.token = authenticate(request)
        self.empresa = self.token.get("empresa_id")
        self.empresas = Empresas.objects.filter(deleted=False) 
        
    def _get_empresa_by_cnpj(self, cnpj):
        return Empresas.objects.filter(cnpj=cnpj, deleted=False)
    
    def get_empresa(self):
        return self.empresas

    def get_empresas_by_id(self, empresa_id: str):
        return Empresas.objects.filter(id=empresa_id)
    
    def create_csv(self, filters):
        datetime_now = datetime.now()  
        path = f'{MEDIA_ROOT}/{self.empresa}'
        empresas = filters.filter(self.empresas)
        dados = format_csv(Empresas)
    
        for itens in empresas:
            valores = [
                        str(itens.deleted), 
                        str(itens.id),
                        str(itens.razao_social),
                        str(itens.nome_fantasia),
                        str(itens.cnpj),
                        str(itens.telefone),
                        str(itens.user_alteracao),
                        str(itens.data_cadastro),
                        str(itens.data_atualizacao),
                      ]
            dados.append(valores)
            
        generate_csv(path, datetime_now, dados)
        
        return FileResponse(open(f'{path}/reports_{datetime_now}.csv', 'rb'), as_attachment=True)
    
    
    def autocomplete_empresa(self, cnpj: str):
        dados_cadastrais = busca_cnpj(cnpj=cnpj)
        if not dados_cadastrais:
            return JsonResponse(data={'error': "CNPJ inválido"}, status=400)  
        return {
            'razao_social': dados_cadastrais["nome"],
            'nome_fantasia': dados_cadastrais["fantasia"],
            'cnpj':cnpj,
            'telefone': dados_cadastrais["telefone"],
            'user_criacao': self.token.get("usuario_id"),
            }   

    def create_empresa(self, payload: EmpresaSchemaIn):
        
        if not payload.cnpj.isdigit():
            return JsonResponse(data={'error': "CNPJ inválido"}, status=400) 
        
        if self._get_empresa_by_cnpj(payload.cnpj).exists():
            return JsonResponse(data={'error': "CNPJ já cadastrado"}, status=400) 
        
        dados = payload.dict()
        dados["user_alteração"] = self.token.get("usuario_id")
        
        empresa = Empresas.objects.create(**dados)
        return JsonResponse(data={"sucess": f'{"Empresa cadastrada com sucesso"} - {empresa.id}'}, status=200)
    
    def update_empresa(self, empresa_id: str, payload: EmpresaSchemaIn):
        empresa = self.get_empresas_by_id(empresa_id=empresa_id)
        if not empresa:
            return JsonResponse(data={'error': "Cadatro inativo"}, status=400)

        dados = payload.dict()
        dados["data_atualizacao"] = datetime.now()
        dados["user_alteracao"] = self.token.get("usuario_id")    
                   
        for attr, value in dados.items():
            setattr(empresa, attr, value)
        empresa.save()
        return JsonResponse(data={"sucess": "Empresa alterada com sucesso"}, status=200)

    def soft_delete_empresa(self, empresa_id: str):
        delete_empresa = Empresas.objects.get(id=empresa_id)
        delete_empresa.soft_delete()
        return JsonResponse(data={"sucess": "Empresa deletada com sucesso"}, status=200)

    def delete_empresa(self, empresa_id: str):
        empresa = Empresas.objects.get(id=empresa_id)
        empresa.delete()
        return JsonResponse(data={"sucess": "Empresa excluida com sucesso"}, status=200)