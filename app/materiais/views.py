from ninja import Router
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from app.materiais.models import Materiais
from app.materiais.schemas import MateriaisSchema
from app.auth import AuthBearer
from app.utils.utils import valores_int

router = Router()
_TGS = ['Materiais']

#GETS
@router.get("/", tags=_TGS, response=list[MateriaisSchema])
def get_itens(request):
    materiais = Materiais.objects.all()   
    for material in materiais:
        material.custo = material.custo/100
        material.preco_revenda = material.preco_revenda/100
    return materiais


@router.get("/{item_id}", tags=_TGS, response=MateriaisSchema)
def get_item_by_id(request, item_id: int):
    material = Materiais.objects.filter(pk=item_id).first()    
    material.custo = material.custo/100
    material.preco_revenda = material.preco_revenda/100
    return material

#POSTS
@router.post("/", tags=_TGS)
def create_item(request, payload:MateriaisSchema):
    payload_dict = {
                    "descricao": payload.descricao,                       
                    "custo": valores_int(payload.custo),
                    "preco_revenda": valores_int(payload.preco_revenda),
                    "empresas_id": payload.empresas_id
                    }
    item = Materiais.objects.create(**payload_dict)
    return JsonResponse({"message": "CREATE", "sucess": f'{"Item cadastrado com sucesso"} - {'id:'}{item.id}'}, status=200)

#PUTS
@router.put("/{item_id}", tags=_TGS)
def update_item(request, item_id: str, payload: MateriaisSchema):
    material = Materiais.objects.filter(id=item_id, deleted=False).first()
    payload_dict = {
                    "descricao": payload.descricao,                       
                    "custo": payload.custo*100,
                    "preco_revenda": payload.preco_revenda*100,
                    "empresas_id": payload.empresas_id
                    }
    if not material:
        return JsonResponse({"error": "Material inativo"}, status=400)
    for attr, value in payload_dict(exclude_unset=True).items():
        setattr(material, attr, value)
    material.save()
    return JsonResponse({"message": "UPDATE", "sucess": "Item alterado com sucesso" }, status=200)

#DELETE
@router.delete("/{item_id}", tags=_TGS, auth=AuthBearer())
def delete_item(request, item_id: int):
    item = get_object_or_404(Materiais, id=item_id)
    item.delete()
    return JsonResponse({"message": "DELETE", "sucess": "Material excluido com sucesso"}, status=200)
