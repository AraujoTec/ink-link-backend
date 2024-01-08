from datetime import datetime
from django.http import JsonResponse
from app.empresas.models import Empresas
from app.empresas.schemas import EmpresaSchemaIn
from app.utils.busca_cnpj import busca_cnpj
from app.utils.jwt_manager import authenticate
import csv
class EmpresasService:
    
    def _get_empresa_by_cnpj(self, cnpj):
        return Empresas.objects.filter(cnpj=cnpj, deleted=False)
    
    def get_empresa(self):
        return Empresas.objects.filter(deleted=False) 

    def get_empresas_by_id(self, empresa_id: str):
        return Empresas.objects.filter(id=empresa_id)
    
    def create_csv(self):
        empresa = self.get_empresa()
        dados = [[
                    'empresa_id',
                    'razao_social',
                    'nome_fantasia',
                    'cnpj',
                    'telefone',
                    'user_alteracao',
                    'data_atualizacao',
                    'data_cadastro',
                    'deleted'
                ],]
    
        for itens in empresa:
            valores = [
                        str(itens.id),
                        str(itens.razao_social),
                        str(itens.nome_fantasia),
                        str(itens.cnpj),
                        str(itens.telefone),
                        str(itens.user_alteracao),
                        str(itens.data_atualizacao),
                        str(itens.data_cadastro),
                        str(itens.deleted) 
                      ]
            dados.append(valores)
    
        with open('/home/gabriel/Documentos/projetos/ink-link-backend/app/utils/docs/relatorios.csv', 'w') as arquivo:
            relatorio_empresa = csv.writer(arquivo)
            for linha in dados:
                relatorio_empresa.writerow(linha)
        
        return JsonResponse(data={"sucess": "Relatório disponibilizado"}, status=200)   
    
    
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
        
        token = authenticate(request) 
        dados = payload.dict()
        dados["user_alteração"] = token.get("usuario_id")
        
        empresa = Empresas.objects.create(**dados)
        return JsonResponse(data={"sucess": f'{"Empresa cadastrada com sucesso"} - {empresa.id}'}, status=200)
    
    def update_empresa(self, request, empresa_id: str, payload: EmpresaSchemaIn):
        empresa = self.get_empresas_by_id(empresa_id=empresa_id)
        if not empresa:
            return JsonResponse(data={'error': "Cadatro inativo"}, status=400)
        
        token = authenticate(request)
        dados = payload.dict()
        dados["data_atualizacao"] = datetime.now()
        dados["user_alteracao"] = token.get("usuario_id")    
                   
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