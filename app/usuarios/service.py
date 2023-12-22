from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from app.usuarios.models import Usuarios
from app.usuarios.schemas import UserSchemaIn, SuperUser
from app.usuarios.models import Usuarios
from app.utils.jwt_manager import authenticate

class UsuariosService:

    def get_user(self, empresa_id):
        return Usuarios.objects.filter(empresa_id=empresa_id, deleted=False) 

    def get_user_by_id(self, request, usuario_id: str):
        token = authenticate(request)
        return Usuarios.objects.filter(id=usuario_id, empresa_id=token.get("empresa_id"), deleted=False)
    
    def get_user_by_email(self, email: str):
        return get_object_or_404(Usuarios, email=email)

    def create_user(self, payload:UserSchemaIn):
        busca_cpf = Usuarios.objects.filter(cpf=payload.cpf)
        if not busca_cpf :
            if payload.cpf.isdigit() == True: 
                user = Usuarios.objects.create_user(**payload.dict())
                return JsonResponse(data={"message": "CREATE", "sucess": f'{"Usuario cadastrado com sucesso"} - {user.id}'}, status=200)
            return JsonResponse(data={'error': "CPF inválido"}, status=400)
        return JsonResponse(data={'error': "CPF já cadastrado"}, status=400)

    def update_user(self, request, usuario_id: str, payload: UserSchemaIn):
        user = self.get_user_by_id(request, usuario_id=usuario_id).first()
        if not user:
            return JsonResponse(data={'error': "Cadastro inativo"}, status=400)
        for attr, value in payload.dict(exclude_unset=True).items():
            setattr(user, attr, value)
        user.save()
        return JsonResponse(data={"message": "UPDATE", "sucess": "Cadastro alterado com sucesso"}, status=200)
        
    def create_super_user(self,request, usuario_id: str, payload:SuperUser):
        user = self.get_user_by_id(request, usuario_id=usuario_id).first()
        for attr, value in payload.dict().items():
            setattr(user, attr, value)
        user.save()
        return JsonResponse(data={"message": "UPDATE", "permissions": list(user.get_all_permissions())}, status=200)

    def soft_delete_user(self,request, usuario_id: str):
        delete_user = self.get_user_by_id(request, usuario_id=usuario_id)
        delete_user.soft_delete()
        return JsonResponse(data={"message": "DELETE", "sucess": "Usuario deletado com sucesso"}, status=200)

    def delete_user(self, request, usuario_id: str):
        user = self.get_user_by_id(request, id=usuario_id)
        user.delete()
        return JsonResponse(data={"message": "DELETE", "sucess": "Usuario excluida com sucesso"}, status=200)

