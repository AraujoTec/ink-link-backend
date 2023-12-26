from ninja import Schema
from uuid import UUID

class DetalheBase(Schema):
    servico_id: UUID
    materiais_id: UUID
    quantidade: int
 
    
class DetalheSchemaOut(DetalheBase):
    id: UUID
    valor_total: float
    lucro_estudio: float
    lucro_colaborador: float
