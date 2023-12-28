from django.http import JsonResponse
from app.materiais.models import Materiais
from app.materiais.schemas import MateriaisSchema
from app.utils.jwt_manager import authenticate
import csv

class MateriaisService:
    
    def get_itens(self, empresa_id: str):
        materiais = Materiais.objects.filter(empresa_id=empresa_id)   
        for material in materiais:
            material.custo = material.custo/100
            material.preco_revenda = material.preco_revenda/100
        return materiais

    def get_item_by_id(self,  item_id: str, empresa_id: str):
        material = Materiais.objects.filter(pk=item_id, empresa_id=empresa_id).first()
        material.custo = material.custo/100
        material.preco_revenda = material.preco_revenda/100
        return material

    def create_csv(self, request):
        token = authenticate(request)
        materiais = Materiais.objects.filter(empresa_id = token.get("empresa_id"))
        dados = [[
                    'material_id',
                    'descricao',
                    'custo',
                    'preco_revenda',
                    'data_validade',
                    'estoque',
                    'empresa'
                ],]
    
        for itens in materiais:
            
            custo = itens.custo / 100
            revenda = itens.preco_revenda / 100
            
            valores = [
                        str(itens.id),  
                        str(itens.descricao),
                        str(custo),
                        str(revenda),
                        str(itens.data_validade),
                        str(itens.estoque),
                        str(itens.empresa)             
                    ]
            dados.append(valores)
    
        with open('/home/gabriel/Documentos/projetos/ink-link-backend/app/utils/docs/relatorios.csv', 'w') as arquivo:
            relatorio_material = csv.writer(arquivo)
            for linha in dados:
                relatorio_material.writerow(linha)
        
        return JsonResponse(data={"sucess": "Relatório disponibilizado"}, status=200)   


    def create_item(self, payload:MateriaisSchema):
        
        dados = payload.dict()
        dados["custo"] = payload.custo*100
        dados["preco_revenda"] = payload.preco_revenda*100
        
        item = Materiais.objects.create(**dados)
        return JsonResponse(data={"sucess": f'{"Item cadastrado com sucesso"} - {'id:'}{item.id}'}, status=200)

    def update_item(self, item_id: str, payload: MateriaisSchema):
        material = Materiais.objects.filter(id=item_id, deleted=False).first()
        
        dados = payload.dict()
        dados["custo"] = payload.custo*100
        dados["preco_revenda"] = payload.preco_revenda*100
        
        if not material:
            return JsonResponse(data={"error": "Material inativo"}, status=400)
        for attr, value in dados(exclude_unset=True).items():
            setattr(material, attr, value)
        material.save()
        return JsonResponse(data={"sucess": "Item alterado com sucesso" }, status=200)

    def delete_item(self, item_id: str):
        item = Materiais.objects.filter(id=item_id, deleted=False).first()
        item.delete()
        return JsonResponse(data={"sucess": "Material excluido com sucesso"}, status=200)
