from ninja import NinjaAPI
from app.usuarios.api import router as usuarios_router
from app.empresas.api import router as empresas_router
from app.materiais.api import router as materiais_router
from app.authenticate.api import router as auth_router

api = NinjaAPI(title="INK-LINK")

api.add_router("/authenticate/", auth_router)
api.add_router("/users/", usuarios_router)
api.add_router("/empresas/", empresas_router)
api.add_router("/materiais/", materiais_router)