from ninja import Schema, FilterSchema, Field
from uuid import UUID
from typing import Optional

class DetalheBase(Schema):
    servico_id: UUID
    materiais_id: UUID
    quantidade: int
 
    
class DetalheSchemaOut(DetalheBase):
    id: UUID
    valor_total: float
    lucro_estudio: float
    lucro_colaborador: float
    
    
class FiltersSchema(FilterSchema):
  id: Optional[str] = None 
  servico:Optional[str] = None
  materiais: Optional[str] = None
  quantidade: Optional[int] = None
    
