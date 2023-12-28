from ninja import Router
from app.authenticate.service import AuthService
from app.authenticate.schemas import LoginSchemaIn

auth_router = Router()
_TGS = ['Auth']

service = AuthService()

#POSTS
@auth_router.post("login", tags=_TGS)
def login(request, payload: LoginSchemaIn):
    response = service.auth_login(request=request, payload=payload)
    return response

@auth_router.post("logout", tags=_TGS)
def logout(request):
    response = service.auth_logout(request)
    return response