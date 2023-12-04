from ninja import Schema
from datetime import date, datetime

class UserSchemaOut(Schema):
    id: int
    nome: str
    email: str
    password: str
    data_cadastro: datetime = None
    data_nascimento: date = None
    ativo: bool
    funcao: str
    cpf: str
    empresa_id: str

    
class UserSchemaIn(Schema):
    nome: str
    email: str
    password: str
    data_cadastro: datetime = None
    data_nascimento: datetime = None
    funcao: str
    cpf: str
    empresa_id: str