from ninja import Router
from django.shortcuts import get_object_or_404
from .models import Empresas
from .schemas import EmpresaSchemaOut, EmpresaSchemaIn
from .buscacnpj import busca_cnpj

router = Router()

@router.get("/", response=list[EmpresaSchemaOut])
def get_empresa(request):
    return Empresas.objects.all() 

@router.get("/{empresa_id}", response=EmpresaSchemaOut)
def get_empresas_by_id(request,empresa_id: int):
    return get_object_or_404(Empresas, pk=empresa_id)

@router.post("/")
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
        return {"id": empresa.id}
    return {"erro": "CNPJ já cadastrado"}

@router.put("/{empresa_id}")
def update_empresa(request, empresa_id: int, payload: EmpresaSchemaIn):
    empresa = get_object_or_404(Empresas, id=empresa_id)
    dados_cadastrais = busca_cnpj(payload.cnpj)
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
    return {"success": True}

@router.delete("/{empresa_id}")
def delete_empresa(request, empresa_id: int):
    empresa = get_object_or_404(Empresas, id=empresa_id)
    empresa.delete()
    return {"success": True}

