from ninja import Router
from app.empresas.service import EmpresasService
from app.empresas.schemas import EmpresaSchemaOut, EmpresaSchemaIn, EmpresaSchemaAuto
from app.authenticate.service import JWTAuth

router = Router(auth=JWTAuth(), tags=['Empresas'])
service = EmpresasService ()

#GETS
@router.get("", response=list[EmpresaSchemaOut])
def get_empresa(request):
    response = service.get_empresa()    
    return response

@router.get("{empresa_id}", response=EmpresaSchemaOut)
def get_empresas_by_id(request, empresa_id: str):
    response = service.get_empresas_by_id(id = empresa_id)
    return response

@router.get("autocomplete/{cnpj}", response=EmpresaSchemaAuto)
def autocomplete_empresa(request, cnpj: str):
    response = service.autocomplete_empresa(request, cnpj=cnpj)
    return response

#POST
@router.post("", auth=None)
def create_empresa(request, payload: EmpresaSchemaIn):
    response = service.create_empresa(payload)
    return response


#PATCH
@router.patch("{empresa_id}")
def update_empresa(request, empresa_id: str, payload: EmpresaSchemaIn):
    response = service.update_empresa(request, empresa_id, payload)
    return response

#DELETE
@router.delete("delete/{empresa_id}")
def soft_delete_empresa(request, empresa_id: str):
    response = service.soft_delete_empresa(empresa_id)
    return response

@router.delete("{empresa_id}")
def delete_empresa(request, empresa_id: str):
    response = service.delete_empresa(empresa_id)
    return response
