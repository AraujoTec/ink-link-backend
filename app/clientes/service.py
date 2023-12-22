from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from app.clientes.models import Clientes
from app.clientes.schemas import ClienteSchemaIn


class ClienteService:

    def get_cliente(self, cliente_id: str):
        return Clientes.objects.filter(id=cliente_id, deleted=False)
    
    def get_cliente_by_id(self, cliente_id: str):
        return Clientes.objects.filter(id=cliente_id, deleted=False)
    
    def get_cliente_by_email(self, email: str):
        return get_object_or_404(Clientes, email=email)

    def create_cliente(self, payload:ClienteSchemaIn):
        busca_cpf = Clientes.objects.filter(cpf=payload.cpf)
        if busca_cpf :
            return JsonResponse(data={'error': "CPF já cadastrado"}, status=400)
        if not payload.cpf.isdigit() == True: 
            return JsonResponse(data={'error': "CPF inválido"}, status=400)
        cliente = Clientes.objects.create_cliente(**payload.dict())
        return JsonResponse(data={"message": "CREATE", "sucess": f'{"Cliente cadastrado com sucesso"} - {cliente.id}'}, status=200)

    def update_cliente(self, cliente_id: str, payload: ClienteSchemaIn):
        cliente = self.get_cliente(cliente_id=cliente_id).first()
        if not cliente:
            return JsonResponse(data={'error': "Cadastro inativo"}, status=400)
        for attr, value in payload.dict(exclude_unset=True).items():
            setattr(cliente, attr, value)
        cliente.save()
        return JsonResponse(data={"message": "UPDATE", "sucess": "Cadastro alterado com sucesso"}, status=200)
        
    def soft_delete_cliente(self, cliente_id: str):
        delete_cliente = self.get_cliente(cliente_id=cliente_id)
        delete_cliente.soft_delete()
        return JsonResponse(data={"message": "DELETE", "sucess": "Usuario deletado com sucesso"}, status=200)

    def delete_cliente(self, cliente_id: str):
        cliente = self.get_cliente(id=cliente_id)
        cliente.delete()
        return JsonResponse(data={"message": "DELETE", "sucess": "Usuario excluida com sucesso"}, status=200)

