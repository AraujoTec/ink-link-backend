from django.http import JsonResponse
from app.clientes.models import Clientes
from app.clientes.schemas import ClienteSchemaIn


class ClienteService:

    def get_cliente(self, empresa_id: str):
        return Clientes.objects.filter(empresa_id=empresa_id)
    
    def get_cliente_by_id(self, cliente_id: str, empresa_id: str):
        return Clientes.objects.filter(id=cliente_id, empresa_id=empresa_id, deleted=False)

    def create_cliente(self, payload:ClienteSchemaIn):
        busca_cpf = Clientes.objects.filter(cpf=payload.cpf)
        if busca_cpf :
            return JsonResponse(data={'error': "CPF já cadastrado"}, status=400)
        if not payload.cpf.isdigit() == True: 
            return JsonResponse(data={'error': "CPF inválido"}, status=400)
        cliente = Clientes.objects.create(**payload.dict())
        return JsonResponse(data={"sucess": f'{"Cliente cadastrado com sucesso"} - {cliente.id}'}, status=200)

    def update_cliente(self, cliente_id: str, empresa_id: str, payload: ClienteSchemaIn):
        cliente = self.get_cliente_by_id(cliente_id=cliente_id, empresa_id=empresa_id).first()
        if not cliente:
            return JsonResponse(data={'error': "Cadastro inativo"}, status=400)
        for attr, value in payload.dict(exclude_unset=True).items():
            setattr(cliente, attr, value)
        cliente.save()
        return JsonResponse(data={"sucess": "Cadastro alterado com sucesso"}, status=200)
        
    def soft_delete_cliente(self, cliente_id: str, empresa_id: str):
        delete_cliente = self.get_cliente_by_id(cliente_id=cliente_id, empresa_id=empresa_id).first()
        delete_cliente.soft_delete()
        return JsonResponse(data={"sucess": "Usuario deletado com sucesso"}, status=200)

    def delete_cliente(self, cliente_id: str, empresa_id: str):
        cliente = self.get_cliente_by_id(cliente_id=cliente_id, empresa_id=empresa_id).first()
        cliente.delete()
        return JsonResponse(data={"sucess": "Usuario excluida com sucesso"}, status=200)

