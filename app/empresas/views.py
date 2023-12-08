from ninja import Router
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from app.empresas.models import Empresas
from app.empresas.schemas import EmpresaSchemaOut, EmpresaSchemaIn, EmpresaSoftDelete
from app.empresas.buscacnpj import busca_cnpj
from app.auth import AuthBearer

router = Router()
_TGS = ['Empresas']

#GETS
@router.get("/",tags=_TGS, response=list[EmpresaSchemaOut])
def get_empresa(request):
    return Empresas.objects.filter(deleted=False) 

@router.get("/{cnpj}",tags=_TGS, response=EmpresaSchemaOut)
def get_empresas_by_id(request,cnpj: str):
    return get_object_or_404(Empresas, cnpj=cnpj)

#POST
@router.post("/",tags=_TGS)
def create_empresa(request, payload: EmpresaSchemaIn):
    dados_cadastrais = busca_cnpj(payload.cnpj)
    input_cnpj = Empresas.objects.filter(cnpj=payload.cnpj)
 
    if not input_cnpj and dados_cadastrais['status'] == "OK":
        payload_dict= {
            'razao_social': dados_cadastrais["nome"],
            'nome_fantasia': dados_cadastrais["fantasia"],
            'cnpj':payload.cnpj,
            'telefone': dados_cadastrais["telefone"],
            'user_criacao': payload.user_criacao,
            "user_alteracao": payload.user_alteracao,
            "data_cadastro": payload.data_cadastro,
            "data_atualizacao": payload.data_atualizacao
            }   
            
        empresa = Empresas.objects.create(**payload_dict)
        return JsonResponse({"message": "CREATE", "sucess": f'{"Empresa cadastrada com sucesso"}-{empresa.uuid}'}, status=200)
    return JsonResponse({'error': "CNPJ já cadastrado"}, status=400)

#PUTS
@router.put("/{cnpj}",tags=_TGS)
def update_empresa(request, cnpj: int, payload: EmpresaSchemaIn):
    dados_cadastrais = busca_cnpj(payload.cnpj)
    empresa = Empresas.objects.filter(cnpj=cnpj, deleted=False).first()
    if not empresa:
        raise JsonResponse({'error': "Cadatro inativo"}, status=400)
    payload_dict= {
        'razao_social': dados_cadastrais["nome"],
        'nome_fantasia': dados_cadastrais["fantasia"],
        'cnpj':payload.cnpj,
        'telefone': dados_cadastrais["telefone"],
        'user_criacao': payload.user_criacao,
        "user_alteracao": payload.user_alteracao,
        "data_cadastro": payload.data_cadastro,
        "data_atualizacao": payload.data_atualizacao
        }   
    
    for attr, value in payload_dict.items():
        setattr(empresa, attr, value)
    empresa.save()
    return JsonResponse({"message": "UPDATE", "sucess": "Empresa alterada com sucesso"}, status=200)

@router.put("/delete/{cnpj}",tags=_TGS)
def soft_delete_user(request, cnpj: str, payload:EmpresaSoftDelete):
    user = get_object_or_404(Empresas, cnpj=cnpj)
    for attr, value in payload.dict().items():
        setattr(user, attr, value)
    user.save()
    if payload.is_active == False and payload.deleted == True:
        delete_user = Empresas.objects.get(cnpj=cnpj)
        delete_user.soft_delete()
    return JsonResponse({"message": "DELETE", "sucess": "Empresa deletada com sucesso"}, status=200)

#DELETE
@router.delete("/{cnpj}", tags=_TGS, auth=AuthBearer())
def delete_empresa(request, cnpj: str):
    empresa = get_object_or_404(Empresas, cnpj=cnpj)
    empresa.delete()
    return JsonResponse({"message": "DELETE", "sucess": "Empresa excluida com sucesso"}, status=200)