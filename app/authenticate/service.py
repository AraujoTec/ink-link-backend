from ninja.security import HttpBearer
from django.http import JsonResponse
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404
from app.authenticate.schemas import LoginSchemaIn
from app.usuarios.models import Usuarios

from app.utils import jwt_manager
from jose import jwt, ExpiredSignatureError
from app import settings

class AuthService():
    
    def auth_login(self, request, payload: LoginSchemaIn):
        self.auth_logout(request)

        user = get_object_or_404(Usuarios, email=payload.email)
        
        if not user:
            return JsonResponse(data={"error": "Invalid credentials"}, status=401)
        
        checkout_password = user.check_password(payload.password)
        
        if not checkout_password:
            return JsonResponse(data={"error": "Invalid credentials"}, status=401)
        
        if user:
            login(request, user)
            token = jwt_manager.generate_jwt_token(usuarios=user)   
            return  JsonResponse(data={"access_token": token, "permissions": list(user.get_all_permissions())}, status=200)
            
        return JsonResponse(data={"error": "Invalid credentials"}, status=401)

    def auth_logout(self, request):
        logout(request)
        return JsonResponse(data={"sucess": "logout user"}, status=200)
    
    
class JWTAuth(HttpBearer):
    
    def authenticate(self, request, token):
        try:
            usuarios = jwt.decode(token, settings.SECRET_KEY)
            request.usuarios = usuarios
            return True
        except ExpiredSignatureError as e:
            raise e
        except:
            return False
        
        
        
