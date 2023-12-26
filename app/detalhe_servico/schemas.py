from ninja import Schema
from uuid import UUID

class DetalheBase(Schema):
    servico_id: UUID
    materiais_id: UUID
    quantidade: str
 
    
class DetalheSchemaOut(DetalheBase):
    id: UUID
    valor_total: str
    lucro_estudio: str
    lucro_colaborador: str
