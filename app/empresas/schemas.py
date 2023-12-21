from ninja import Schema
from datetime import datetime
from uuid import UUID
class EmpresaSchemaBase(Schema):
    cnpj: str
    razao_social: str
    nome_fantasia: str
    telefone: str

class EmpresaSchemaOut(EmpresaSchemaBase):
    id: UUID
    user_alteracao: str
    data_cadastro: datetime = None
    data_atualizacao: datetime = None

class EmpresaSchemaAuto(EmpresaSchemaBase):
    pass
    
class EmpresaSchemaIn(EmpresaSchemaBase):
    pass
