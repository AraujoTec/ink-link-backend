from django.http import JsonResponse
from app.clientes.models import Clientes
from app.clientes.schemas import ClienteSchemaIn
from app.utils.jwt_manager import authenticate
import csv
class ClienteService:

    def get_cliente(self, empresa_id: str):
        return Clientes.objects.filter(empresa_id=empresa_id)
    
    def get_cliente_by_id(self, cliente_id: str, empresa_id: str):
        return Clientes.objects.filter(id=cliente_id, empresa_id=empresa_id, deleted=False)

    def create_csv(self, request):
        token = authenticate(request)
        cliente = self.get_cliente(token.get("empresa_id"))
        dados = [[
                    'cliente_id',
                    'nome',
                    'empresa',
                    'colaborador',
                    'servico',
                    'forma_pagamento',
                    'data_nascimento',
                    'cpf',
                    'cep',
                    'telefone',
                    'instagram'
                ],]
    
        for itens in cliente:
            valores = [
                        str(itens.id),  
                        f'{str(itens.first_name)} {itens.last_name}',
                        str(itens.empresa),
                        str(itens.colaborador),
                        str(itens.servico),
                        str(itens.forma_pagamento),
                        str(itens.data_nascimento),
                        str(itens.cpf),
                        str(itens.cep),
                        str(itens.telefone),
                        str(itens.instagram)                
                    ]
            dados.append(valores)
    
        with open('/home/gabriel/Documentos/projetos/ink-link-backend/app/utils/docs/relatorios.csv', 'w') as arquivo:
            relatorio_cliente = csv.writer(arquivo)
            for linha in dados:
                relatorio_cliente.writerow(linha)
        
        return JsonResponse(data={"sucess": "Relatório disponibilizado"}, status=200)

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

