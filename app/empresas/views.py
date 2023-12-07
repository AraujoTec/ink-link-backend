from ninja import Router
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from app.empresas.models import Empresas
from app.empresas.schemas import EmpresaSchemaOut, EmpresaSchemaIn, EmpresaSoftDelete
from app.empresas.buscacnpj import busca_cnpj
from app.auth import AuthBearer

router = Router()
_TGS = ['CRUD Empresas']

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
        return 200, {"message": "CREATE", "sucess": f'{"Empresa cadastrada com sucesso"}-{empresa.uuid}'}
    return HttpError(400, "CPF já cadastrado")

#PUTS
@router.put("/{cnpj}",tags=_TGS)
def update_empresa(request, cnpj: int, payload: EmpresaSchemaIn):
    empresa = get_object_or_404(Empresas, cnpj=cnpj)
    dados_cadastrais = busca_cnpj(payload.cnpj)
    lista_empresas = list(Empresas.objects.filter(deleted=False))
    if empresa in lista_empresas:
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
        return 200, {"message": "UPDATE", "sucess": "Empresa alterada com sucesso" }
    raise HttpError(404, "Empresa inativa")

@router.put("/delete/{cnpj}",tags=_TGS)
def soft_delete_user(request, cnpj: str, payload:EmpresaSoftDelete):
    user = get_object_or_404(Empresas, cnpj=cnpj)
    for attr, value in payload.dict().items():
        setattr(user, attr, value)
    user.save()
    if payload.is_active == False and payload.deleted == True:
        delete_user = Empresas.objects.get(cnpj=cnpj)
        delete_user.soft_delete()
    return 200, {"message": "DELETE", "sucess": "Empresa deletada com sucesso"}

#DELETE
@router.delete("/{cnpj}", tags=_TGS, auth=AuthBearer())
def delete_empresa(request, cnpj: str):
    empresa = get_object_or_404(Empresas, cnpj=cnpj)
    empresa.delete()
    return 200, {"message": "DELETE", "sucess": "Empresa deletada com sucesso"}
