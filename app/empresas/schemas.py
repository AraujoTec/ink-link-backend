from ninja import Schema
from datetime import datetime

class EmpresaSchemaOut(Schema):
    uuid: int
    razao_social: str
    nome_fantasia: str
    cnpj: str
    telefone: str
    user_criacao: str
    user_alteracao: str
    data_cadastro: datetime = None
    data_atualizacao: datetime = None
    
class EmpresaSchemaIn(Schema):
    cnpj: str
    user_criacao: str
    user_alteracao: str
    data_cadastro: datetime = None
    data_atualizacao: datetime = None
class EmpresaSoftDelete(Schema):
    deleted: bool = True