from ninja import Schema

class LoginSchemaIn(Schema):
    email: str
    password: str
    
    
    