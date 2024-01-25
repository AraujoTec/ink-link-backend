from ninja import Router, Query
from app.empresas.service import EmpresasService
from app.empresas.schemas import EmpresaSchemaOut, EmpresaSchemaIn, EmpresaSchemaAuto, FiltersSchema
from app.authenticate.service import JWTAuth

empresas_router = Router(auth=JWTAuth(), tags=['Empresas'])

#GETS
@empresas_router.get("", response=list[EmpresaSchemaOut], auth=None)
def get_empresa(request):
    service = EmpresasService(request)
    return service.get_empresa()    
    
@empresas_router.get("{empresa_id}", response=EmpresaSchemaOut, auth=None)
def get_empresas_by_id(request, empresa_id: str):
    service = EmpresasService(request)
    return service.get_empresas_by_id(empresa_id)
    

@empresas_router.get("autocomplete/{cnpj}", response=EmpresaSchemaAuto, auth=None)
def autocomplete_empresa(request, cnpj: str):
    service = EmpresasService(request)
    return service.autocomplete_empresa(cnpj)
    
@empresas_router.get("reports/")
def create_csv(request, filters: FiltersSchema = Query(...)):
    service = EmpresasService(request)
    return service.create_csv(filters)

#POST
@empresas_router.post("")
def create_empresa(request, payload: EmpresaSchemaIn):
    service = EmpresasService(request)
    return service.create_empresa(payload)
    

#PATCH
@empresas_router.patch("{empresa_id}")
def update_empresa(request, empresa_id: str, payload: EmpresaSchemaIn):
    service = EmpresasService(request)
    return service.update_empresa(empresa_id, payload)
    

#DELETE
@empresas_router.delete("delete/{empresa_id}")
def soft_delete_empresa(request, empresa_id: str):
    service = EmpresasService(request)
    return service.soft_delete_empresa(empresa_id)
    

@empresas_router.delete("{empresa_id}")
def delete_empresa(request, empresa_id: str):
    service = EmpresasService(request)
    return service.delete_empresa(empresa_id)
    
