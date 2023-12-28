from ninja import Router
from app.empresas.service import EmpresasService
from app.empresas.schemas import EmpresaSchemaOut, EmpresaSchemaIn, EmpresaSchemaAuto
from app.authenticate.service import JWTAuth
from app.utils.jwt_manager import authenticate
from django.http import JsonResponse


empresas_router = Router(auth=JWTAuth(), tags=['Empresas'])
service = EmpresasService ()

#GETS
@empresas_router.get("", response=list[EmpresaSchemaOut], auth=None)
def get_empresa(request):
    return service.get_empresa()    
    

@empresas_router.get("{empresa_id}", response=EmpresaSchemaOut, auth=None)
def get_empresas_by_id(request, empresa_id: str):
    return service.get_empresas_by_id(id = empresa_id)
    

@empresas_router.get("autocomplete/{cnpj}", response=EmpresaSchemaAuto, auth=None)
def autocomplete_empresa(request, cnpj: str):
    return service.autocomplete_empresa(request, cnpj=cnpj)
    

#POST
@empresas_router.post("")
def create_empresa(request, payload: EmpresaSchemaIn):
    return service.create_empresa(request, payload)
    

#PATCH
@empresas_router.patch("{empresa_id}")
def update_empresa(request, empresa_id: str, payload: EmpresaSchemaIn):
    token = authenticate(request)    
    if not token.get("empresa_id") == empresa_id and token.get("is_superuser") == True:
        return JsonResponse(data={'error': "usuário inválido"}, status=400)
    return service.update_empresa(request, empresa_id, payload)
    

#DELETE
@empresas_router.delete("delete/{empresa_id}")
def soft_delete_empresa(request, empresa_id: str):
    token = authenticate(request)    
    if not token.get("empresa_id") == empresa_id and token.get("is_superuser") == True:
        return JsonResponse(data={'error': "usuário inválido"}, status=400)
    return service.soft_delete_empresa(empresa_id)
    

@empresas_router.delete("{empresa_id}")
def delete_empresa(request, empresa_id: str):
    token = authenticate(request)    
    if not token.get("empresa_id") == empresa_id and token.get("is_superuser") == True:
        return JsonResponse(data={'error': "usuário inválido"}, status=400)
    return service.delete_empresa(empresa_id)
    
