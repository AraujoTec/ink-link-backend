from ninja import NinjaAPI
from app.usuarios.api import usuarios_router
from app.empresas.api import empresas_router
from app.materiais.api import materiais_router
from app.authenticate.api import auth_router
from app.cargos.api import cargos_router

api = NinjaAPI(title="INK-LINK")

api.add_router("/authenticate/", auth_router)
api.add_router("/users/", usuarios_router)
api.add_router("/empresas/", empresas_router)
api.add_router("/materiais/", materiais_router)
api.add_router("/cargos/", cargos_router)
