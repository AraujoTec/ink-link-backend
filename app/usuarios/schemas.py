from ninja import Schema, FilterSchema, Field
from datetime import date, datetime
from uuid import UUID
from typing import Optional

class UserSchemaBase(Schema):
    first_name: str
    last_name: str
    cpf: str
    data_nascimento: date = None
    empresa_id: UUID
    cargo_id: UUID
    email: str
    password: str
    is_staff: bool = True
class UserSchemaOut(UserSchemaBase):
    id: UUID
    last_login: datetime = None
    date_joined: datetime = datetime.now()
    is_superuser: bool = False
    is_active: bool = True
    deleted: bool = False
        
class UserSchemaIn(UserSchemaBase):
    pass

class FiltersSchema(FilterSchema):
    id: Optional[UUID] = None
    first_name: Optional[str] = Field(None, q='first_name__icontains')
    last_name: Optional[str] = Field(None, q='last_name__icontains')
    cpf: Optional[str] = Field(None, q='cpf__icontains')
    empresa_id: Optional[UUID] = None
    cargo_id: Optional[UUID] = None
    is_superuser: Optional[bool] = any
    is_active: Optional[bool] = any
    deleted: Optional[bool] = any
    email:Optional[str] = Field(None, q='email__icontains')