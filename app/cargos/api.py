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
    return service.get_cargo(empresa_id=token.get("empresa_id"))    
    

#POST
@cargos_router.post("cargo")
def create_cargo(request, payload: CargoSchema):
    return service.create_cargo(request, payload)
    

#DELETE
@cargos_router.delete("{cargo_id}")
def delete_cargo(request, cargo_id: str):
    return service.delete_cargo(request, cargo_id)
    

