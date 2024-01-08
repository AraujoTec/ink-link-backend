from ninja import Schema
from datetime import datetime, date
from uuid import UUID
class MateriaisSchema(Schema):
    descricao: str
    custo: float
    preco_revenda: float
    empresa_id: UUID
    data_validade: date = None
    estoque: int
    
class MateriaisSchemaOut(MateriaisSchema):  
    data_criacação: datetime = datetime.now()