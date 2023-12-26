from ninja import Schema
from uuid import UUID

class ServicoSchema(Schema):
    servico: str
    empresa_id: UUID
    valor: float
    
class ServicoSchemaOut(ServicoSchema):
    id: UUID