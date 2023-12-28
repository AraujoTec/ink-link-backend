from django.http import JsonResponse
from app.usuarios.models import Usuarios
from app.usuarios.schemas import UserSchemaIn
from app.utils.jwt_manager import authenticate
import csv
class UsuariosService:

    def get_user(self, empresa_id: str):
        return Usuarios.objects.filter(empresa_id=empresa_id, deleted=False) 

    def get_user_by_id(self, request, usuario_id: str):
        token = authenticate(request)
        return Usuarios.objects.filter(id=usuario_id, empresa_id=token.get("empresa_id"), deleted=False)

    def create_csv(self, request):
        token = authenticate(request)
        colaborador = self.get_user(token.get("empresa_id"))
        dados = [[
                    'colaborador_id',
                    'nome',
                    'empresa',
                    'cargo',
                    'data_nascimento',
                    'cpf'
                ],]
    
        for itens in colaborador:
            valores = [
                        str(itens.id),  
                        f'{str(itens.first_name)} {itens.last_name}',
                        str(itens.empresa),
                        str(itens.cargo),

                        str(itens.data_nascimento),
                        str(itens.cpf)               
                     ]
            dados.append(valores)
    
        with open('/home/gabriel/Documentos/projetos/ink-link-backend/app/utils/docs/relatorios.csv', 'w') as arquivo:
            relatorio_colaborador = csv.writer(arquivo)
            for linha in dados:
                relatorio_colaborador.writerow(linha)
        
        return JsonResponse(data={"sucess": "Relatório disponibilizado"}, status=200)   

    def create_user(self, payload:UserSchemaIn):
        busca_cpf = Usuarios.objects.filter(cpf=payload.cpf)
        if busca_cpf :
            return JsonResponse(data={'error': "CPF já cadastrado"}, status=400)
        if not payload.cpf.isdigit() == True: 
            return JsonResponse(data={'error': "CPF inválido"}, status=400)
        user = Usuarios.objects.create_user(**payload.dict())
        return JsonResponse(data={"sucess": f'{"Usuario cadastrado com sucesso"} - {user.id}'}, status=200)

    def update_user(self, request, usuario_id: str, payload: UserSchemaIn):
        user = self.get_user_by_id(request, usuario_id=usuario_id).first()
        if not user:
            return JsonResponse(data={'error': "Cadastro inativo"}, status=400)
        for attr, value in payload.dict(exclude_unset=True).items():
            setattr(user, attr, value)
        user.save()
        return JsonResponse(data={"sucess": "Cadastro alterado com sucesso"}, status=200)
        
    def create_super_user(self,request, usuario_id: str):
        user = self.get_user_by_id(request, usuario_id=usuario_id).first()
        dados = {"is_superuser": True}    
        for attr, value in dados.items():
            setattr(user, attr, value)
        user.save()
        return JsonResponse(data={"permissions": list(user.get_all_permissions())}, status=200)

    def soft_delete_user(self,request, usuario_id: str):
        delete_user = self.get_user_by_id(request, usuario_id=usuario_id).first()
        delete_user.soft_delete()
        return JsonResponse(data={"sucess": "Usuario deletado com sucesso"}, status=200)

    def delete_user(self, request, usuario_id: str):
        user = self.get_user_by_id(request, usuario_id=usuario_id).first()
        user.delete()
        return JsonResponse(data={"sucess": "Usuario excluida com sucesso"}, status=200)

