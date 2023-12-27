from ninja import Schema
from datetime import date, datetime
from uuid import UUID


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

    
    