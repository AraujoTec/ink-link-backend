from ninja import Schema
from datetime import date, datetime
from uuid import UUID


class UserSchemaBase(Schema):
    first_name: str
    last_name: str
    cpf: str
    data_nascimento: date = None
    empresa_id: str
    cargo_id: str
    email: str
    password: str
    is_staff: bool = True
class UserSchemaOut(UserSchemaBase):
    id: UUID
    last_login: datetime = None
    date_joined: datetime = datetime.now()
    is_superuser: bool = False
    is_active: bool = True
    deleted: bool
        
class UserSchemaIn(UserSchemaBase):
    pass
class SuperUser(Schema):
    is_superuser: bool = True
    

    
    