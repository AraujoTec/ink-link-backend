from ninja import Router
from app.cargos.service import CargosService
from app.cargos.schemas import CargoSchema, CargoSchemaOut
from app.authenticate.service import JWTAuth
from app.utils.jwt_manager import authenticate

cargos_router = Router(auth=JWTAuth(), tags=['Cargos'])

#GETS
@cargos_router.get("", response=list[CargoSchemaOut])
def get_cargo(request):
    service = CargosService(request)
    return service.get_cargo()    
    
#POST
@cargos_router.post("cargo")
def create_cargo(request, payload: CargoSchema):
    service = CargosService(request)
    return service.create_cargo(payload)
    

#DELETE
@cargos_router.delete("{cargo_id}")
def delete_cargo(request, cargo_id: str):
    service = CargosService(request)
    return service.delete_cargo(cargo_id)
    

