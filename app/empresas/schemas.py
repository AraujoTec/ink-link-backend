from ninja import Schema
from datetime import datetime

class EmpresaSchemaOut(Schema):
    id: int
    razao_social: str
    nome_fantasia: str
    cnpj: str
    telefone: str
    user_criacao: str
    user_alteracao: str
    data_cadastro: datetime = None
    data_atualizacao: datetime = None
    excluido: bool
    
    
class EmpresaSchemaIn(Schema):
    # razao_social: str
    # nome_fantasia: str
    cnpj: str
    # telefone: str
    user_criacao: str
    user_alteracao: str
    data_cadastro: datetime = None
    data_atualizacao: datetime = None
  
    