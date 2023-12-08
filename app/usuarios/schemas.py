from ninja import Schema
from datetime import date, datetime

class UserSchemaOut(Schema):
    uuid: str
    first_name: str
    last_name: str
    username: str
    cpf: str
    data_nascimento: date = None   
    empresas_id: str
    funcao: str
    email: str
    password: str  
    last_login: datetime = None
    date_joined: datetime = datetime.now()
    is_superuser: bool = False
    is_staff: bool = True
    is_active: bool = True
    deleted: bool
    
class UserSchemaIn(Schema):
    username: str
    first_name: str
    last_name: str
    funcao: str
    cpf: str
    data_nascimento: date = None
    is_staff: bool = True
    empresas_id: str
    email: str
    password: str
    
class UserUpdate(Schema):
    username: str
    first_name: str
    last_name: str
    funcao: str
    cpf: str
    data_nascimento: date = None
    is_staff: bool = True
    empresas_id: int

class UserSoftDelete(Schema):
    is_active: bool = False
    deleted: bool = True
    
class SuperUser(Schema):
    is_superuser: bool = True
    
    

    
    