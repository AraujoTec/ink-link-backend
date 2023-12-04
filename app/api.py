from ninja import NinjaAPI
from app.usuarios.views import router as usuarios_router
from app.empresas.views import router as empresas_router
from ninja_auth.api import router as auth_router


api = NinjaAPI(csrf=True)

api.add_router('/auth/' ,  auth_router)
api.add_router("/users/", usuarios_router)
api.add_router("/empresas/", empresas_router)
