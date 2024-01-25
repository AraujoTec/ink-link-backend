from ninja import Schema, FilterSchema, Field
from datetime import date, datetime
from uuid import UUID
from typing import Optional


class ClienteSchemaBase(Schema):
    first_name: str
    last_name: str
    cpf: str
    data_nascimento: date = None
    email: str
    password: str
    is_staff: bool = True
    cep: str = None
    instagram: str = None

class ClienteSchemaOut(ClienteSchemaBase):
    id: UUID
    last_login: datetime = None
    date_joined: datetime = datetime.now()
    is_active: bool = True
    deleted: bool
        
class ClienteSchemaIn(ClienteSchemaBase):
    servico_id: UUID
    colaborador_id: UUID
    forma_pagamento_id: UUID
    empresa_id: UUID

class FiltersSchema(FilterSchema):
    id: Optional[str] = Field(None, q='id__icontains')
    servico_id: Optional[str] = Field(None, q='servico_id__icontains')
    empresa_id: Optional[str] = Field(None, q='empresa_id__icontains')
    cpf: Optional[str] = Field(None, q='cpf__icontains')
    email: Optional[str] = Field(None, q='email__icontains')
    data_nascimento: Optional[date] = Field(None, q='data_nascimento__icontains')
   