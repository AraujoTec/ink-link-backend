from ninja import Router
from django.http import FileResponse
from app.empresas.service import EmpresasService
from app.empresas.schemas import EmpresaSchemaOut, EmpresaSchemaIn, EmpresaSchemaAuto
from app.authenticate.service import JWTAuth

empresas_router = Router(auth=JWTAuth(), tags=['Empresas'])
service = EmpresasService ()

#GETS
@empresas_router.get("", response=list[EmpresaSchemaOut], auth=None)
def get_empresa(request):
    return service.get_empresa()    
    
@empresas_router.get("{empresa_id}", response=EmpresaSchemaOut, auth=None)
def get_empresas_by_id(request, empresa_id: str):
    return service.get_empresas_by_id(empresa_id)
    

@empresas_router.get("autocomplete/{cnpj}", response=EmpresaSchemaAuto, auth=None)
def autocomplete_empresa(request, cnpj: str):
    return service.autocomplete_empresa(request, cnpj)
    
@empresas_router.get("relatorio/")
def create_csv(request):
    service.create_csv()
    return FileResponse(open("/home/gabriel/Documentos/projetos/ink-link-backend/app/utils/docs/relatorios.csv", 'rb'), as_attachment=True)

#POST
@empresas_router.post("")
def create_empresa(request, payload: EmpresaSchemaIn):
    return service.create_empresa(request, payload)
    

#PATCH
@empresas_router.patch("{empresa_id}")
def update_empresa(request, empresa_id: str, payload: EmpresaSchemaIn):
    return service.update_empresa(request, empresa_id, payload)
    

#DELETE
@empresas_router.delete("delete/{empresa_id}")
def soft_delete_empresa(request, empresa_id: str):
   
    return service.soft_delete_empresa(empresa_id)
    

@empresas_router.delete("{empresa_id}")
def delete_empresa(request, empresa_id: str):
    return service.delete_empresa(empresa_id)
    
