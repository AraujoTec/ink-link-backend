from ninja import Schema, FilterSchema, Field
from datetime import datetime, date
from uuid import UUID
from typing import Optional
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

class FiltersSchema(FilterSchema):
    id: Optional[str] = None
    cnpj: Optional[str] = Field(None, q='cnpj__icontains')
    razao_social: Optional[str] = Field(None, q='razao_social__icontains')
    nome_fantasia: Optional[str] = Field(None, q='nome_fantasia__icontains')
    user_alteracao: Optional[str] = Field(None, q='user_alteracao__icontains')
    data_cadastro: Optional[date] = Field(None, q='data_cadastro__icontains')
    data_atualizacao: Optional[date] = Field(None, q='data_atualizacao__icontains')
   