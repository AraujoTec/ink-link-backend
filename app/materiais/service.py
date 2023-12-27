from django.http import JsonResponse
from app.materiais.models import Materiais
from app.materiais.schemas import MateriaisSchema


class MateriaisService:
    
    def get_itens(request, empresa_id: str):
        materiais = Materiais.objects.filter(empresa_id=empresa_id)   
        for material in materiais:
            material.custo = material.custo/100
            material.preco_revenda = material.preco_revenda/100
        return materiais

    def get_item_by_id(request, item_id: str, empresa_id):
        material = Materiais.objects.filter(pk=item_id, empresa_id=empresa_id).first()
        material.custo = material.custo/100
        material.preco_revenda = material.preco_revenda/100
        return material

    def create_item(request, payload:MateriaisSchema):
        
        dados = payload.dict()
        dados["custo"] = payload.custo*100
        dados["preco_revenda"] = payload.preco_revenda*100
        
        item = Materiais.objects.create(**dados)
        return JsonResponse(data={"sucess": f'{"Item cadastrado com sucesso"} - {'id:'}{item.id}'}, status=200)

    def update_item(request, item_id: str, payload: MateriaisSchema):
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

    def delete_item(request, item_id: str):
        item = Materiais.objects.filter(id=item_id, deleted=False).first()
        item.delete()
        return JsonResponse(data={"sucess": "Material excluido com sucesso"}, status=200)
