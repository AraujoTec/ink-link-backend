from ninja import NinjaAPI, Schema

from .models import Empresa
from .schemas import EmpresaSchema

import json

api = NinjaAPI()

@api.get("/empresas", response=list[EmpresaSchema])
def get_empresa(request):

    empresa = Empresa.objects.all()   
    return empresa
 

@api.get("/empresa/{empresa_id}", response=EmpresaSchema)
def get_by_id(request,empresa_id: int):
   
    empresa = Empresa.objects.get(pk=empresa_id)
    return empresa
