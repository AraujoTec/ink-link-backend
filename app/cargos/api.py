from ninja import Router
from app.cargos.service import CargosService
from app.cargos.schemas import CargoSchema, CargoSchemaOut
from app.authenticate.service import JWTAuth
from app.utils.jwt_manager import authenticate

cargos_router = Router(auth=JWTAuth(), tags=['Cargos'])
service = CargosService ()

#GETS
@cargos_router.get("", response=list[CargoSchemaOut])
def get_cargo(request):
    token = authenticate(request)
    response = service.get_cargo(empresa_id=token.get("empresa_id"))    
    return response

#POST
@cargos_router.post("cargo")
def create_cargo(request, payload: CargoSchema):
    response = service.create_cargo(request, payload)
    return response

#DELETE
@cargos_router.delete("{id}")
def delete_cargo(request, id: str):
    response = service.delete_cargo(request, id)
    return response

