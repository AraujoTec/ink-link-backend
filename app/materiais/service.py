from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from app.materiais.models import Materiais
from app.materiais.schemas import MateriaisSchema
from app.utils.jwt_manager import authenticate

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
        
        payload_dict = payload.dict()
        payload_dict["custo"] = payload.custo*100
        payload_dict["preco_revenda"] = payload.preco_revenda*100
        
        item = Materiais.objects.create(**payload_dict)
        return JsonResponse(data={"message": "CREATE", "sucess": f'{"Item cadastrado com sucesso"} - {'id:'}{item.id}'}, status=200)

    def update_item(request, item_id: str, payload: MateriaisSchema):
        material = Materiais.objects.filter(id=item_id, deleted=False).first()
        
        payload_dict = payload.dict()
        payload_dict["custo"] = payload.custo*100
        payload_dict["preco_revenda"] = payload.preco_revenda*100
        
        if not material:
            return JsonResponse(data={"error": "Material inativo"}, status=400)
        for attr, value in payload_dict(exclude_unset=True).items():
            setattr(material, attr, value)
        material.save()
        return JsonResponse(data={"message": "UPDATE", "sucess": "Item alterado com sucesso" }, status=200)

    def delete_item(request, item_id: str):
        item = get_object_or_404(Materiais, id=item_id)
        item.delete()
        return JsonResponse(data={"message": "DELETE", "sucess": "Material excluido com sucesso"}, status=200)
