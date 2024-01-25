from datetime import datetime
from django.http import JsonResponse, FileResponse
from app.settings import MEDIA_ROOT
from app.usuarios.models import Usuarios
from app.usuarios.schemas import UserSchemaIn
from app.utils.jwt_manager import authenticate
from app.utils.csv import generate_csv
class UsuariosService:

    def __init__(self, request):
        self.token = authenticate(request)
        self.empresa = self.token.get("empresa_id")
        self.usuario = self.token.get("usuario_id")

    def get_user(self):
        return Usuarios.objects.filter(empresa_id=self.empresa, deleted=False) 

    def get_user_by_id(self, usuario_id: str):
        return Usuarios.objects.filter(id=usuario_id, empresa_id=self.empresa, deleted=False)

    def create_csv(self, filters):
        datetime_now = datetime.now()  
        path = f'{MEDIA_ROOT}/{self.empresa}'
        colaborador = filters.filter(self.get_user())
        
        dados = [[
                    'colaborador_id',
                    'nome',
                    'empresa',
                    'cargo',
                    'email',
                    'data_nascimento',
                    'cpf', 
                    'is_superuser',
                    'date_joined',
                ],]
        
        for itens in colaborador:
            valores = [
                        str(itens.id),  
                        f'{str(itens.first_name)} {itens.last_name}',
                        str(itens.empresa),
                        str(itens.cargo),
                        str(itens.email),
                        str(itens.data_nascimento),
                        str(itens.cpf),
                        str(itens.is_superuser),
                        str(itens.date_joined)               
                     ]
            
            dados.append(valores)
    
        generate_csv(path, datetime_now, dados)

        return FileResponse(open(f'{path}/reports_{datetime_now}.csv', 'rb'), as_attachment=True)

    def create_user(self, payload:UserSchemaIn):
        busca_cpf = Usuarios.objects.filter(cpf=payload.cpf)
        if busca_cpf :
            return JsonResponse(data={'error': "CPF já cadastrado"}, status=400)
        
        if not payload.cpf.isdigit() == True: 
            return JsonResponse(data={'error': "CPF inválido"}, status=400)
        
        user = Usuarios.objects.create_user(**payload.dict())
        return JsonResponse(data={"sucess": f'{"Usuario cadastrado com sucesso"} - {user.id}'}, status=200)

    def update_user(self, usuario_id: str, payload: UserSchemaIn):
        user = self.get_user_by_id(usuario_id=usuario_id).first()
        if not user:
            return JsonResponse(data={'error': "Cadastro inativo"}, status=400)
        
        for attr, value in payload.dict(exclude_unset=True).items():
            setattr(user, attr, value)
            
        user.save()
        return JsonResponse(data={"sucess": "Cadastro alterado com sucesso"}, status=200)
        
    def create_super_user(self, usuario_id: str):
        user = self.get_user_by_id(usuario_id=usuario_id).first()
        dados = {"is_superuser": True}   
         
        for attr, value in dados.items():
            setattr(user, attr, value)
            
        user.save()
        return JsonResponse(data={"permissions": list(user.get_all_permissions())}, status=200)

    def soft_delete_user(self, usuario_id: str):
        delete_user = self.get_user_by_id(usuario_id=usuario_id).first()
        delete_user.soft_delete()
        return JsonResponse(data={"sucess": "Usuario deletado com sucesso"}, status=200)

    def delete_user(self, usuario_id: str):
        user = self.get_user_by_id(usuario_id=usuario_id).first()
        user.delete()
        return JsonResponse(data={"sucess": "Usuario excluida com sucesso"}, status=200)

