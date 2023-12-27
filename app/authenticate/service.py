from ninja.security import HttpBearer
from django.contrib.auth import login, logout
from django.http import JsonResponse
from datetime import datetime
from jose import jwt, ExpiredSignatureError
from app import settings
from app.authenticate.schemas import LoginSchemaIn
from app.authenticate.models import User
from app.utils import jwt_manager

class AuthService():
    
    def auth_login(self, request, payload: LoginSchemaIn):
        self.auth_logout(request)
        
        user = User.objects.filter(email=payload.email).first()
        
        if not user:
            return JsonResponse(data={"error": "Invalid credentials"}, status=401)
        
        checkout_password = user.check_password(payload.password)
        
        if not checkout_password:
            return JsonResponse(data={"error": "Invalid credentials"}, status=401)
        
        if user:
            login(request, user)
            
            dados = {"last_login": datetime.now()}    
            for attr, value in dados.items():
                setattr(user, attr, value)
            user.save()
                        
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
        
        
        
