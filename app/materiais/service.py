from datetime import datetime
from django.http import JsonResponse, FileResponse
from app.settings import MEDIA_ROOT
from app.materiais.models import Materiais
from app.materiais.schemas import MateriaisSchema
from app.utils.jwt_manager import authenticate
from app.utils.csv import format_csv, generate_csv

class MateriaisService:
    
    def __init__(self, request):
        self.token = authenticate(request)
        self.empresa = self.token.get("empresa_id")
        self.materiais = Materiais.objects.filter(empresa_id=self.empresa)

    def get_material(self, item_id: str):
        return Materiais.objects.filter(pk=item_id, empresa_id= self.empresa, deleted=False).first()
        
    def get_itens(self, request):
        service = MateriaisService(request)
        materiais = self.materiais
        for material in materiais:
            material.custo = material.custo/100
            material.preco_revenda = material.preco_revenda/100
        return materiais

    def get_item_by_id(self, request, item_id: str ):
        service = MateriaisService(request)
        material = service.get_material(item_id)
        material.custo = material.custo/100
        material.preco_revenda = material.preco_revenda/100
        return material

    def create_csv(self, request, filters):
        service = MateriaisService(request)
        datetime_now = datetime.now()  
        path = f'{MEDIA_ROOT}/{self.empresa}'
        
        materiais = filters.filter(self.materiais)
        
        dados = format_csv(Materiais)
    
        for itens in materiais:
            
            custo = itens.custo/100
            revenda = itens.preco_revenda/100
            
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
        
        generate_csv(path, datetime_now, dados)
        
        return FileResponse(open(f'{path}/reports_{datetime_now}.csv', 'rb'), as_attachment=True)


    def create_item(self, request, payload:MateriaisSchema):
        service = MateriaisService(request)
        
        if not self.empresa == str(payload.empresa_id):
            return JsonResponse(data={'error': "usuário inválido"}, status=400)
            
        dados = payload.dict()
        dados["custo"] = payload.custo*100
        dados["preco_revenda"] = payload.preco_revenda*100
        
        item = Materiais.objects.create(**dados)
        return JsonResponse(data={"sucess": f'{"Item cadastrado com sucesso"} - {'id:'}{item.id}'}, status=200)

    def update_item(self, request, item_id: str, payload: MateriaisSchema):
        service = MateriaisService(request)
        
        if not self.empresa == str(payload.empresa_id):
            return JsonResponse(data={'error': "usuário inválido"}, status=400)
        
        material = service.get_material(item_id)
                
        dados = payload.dict()
        dados["custo"] = payload.custo*100
        dados["preco_revenda"] = payload.preco_revenda*100
        
        if not material:
            return JsonResponse(data={"error": "Material inativo"}, status=400)
        
        for attr, value in dados(exclude_unset=True).items():
            setattr(material, attr, value)
        material.save()
        return JsonResponse(data={"sucess": "Item alterado com sucesso" }, status=200)

    def delete_item(self, request, item_id: str):
        service = MateriaisService(request)
        
        if not self.empresa:
            return JsonResponse(data={'error': "usuário inválido"}, status=400)
        
        material = service.get_material(item_id)
        material.delete()
        
        return JsonResponse(data={"sucess": "Material excluido com sucesso"}, status=200)
