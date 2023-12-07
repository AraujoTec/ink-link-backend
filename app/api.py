from ninja import NinjaAPI
from app.usuarios.views import router as usuarios_router
from app.empresas.views import router as empresas_router

api = NinjaAPI()

api.add_router("/users/", usuarios_router)
api.add_router("/empresas/", empresas_router)
