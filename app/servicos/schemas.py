from ninja import Schema
from uuid import UUID

class ServicoSchema(Schema):
    servico: str
    valor: float
    
class ServicoSchemaOut(ServicoSchema):
    id: UUID
    empresa_id: UUID