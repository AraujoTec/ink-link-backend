from ninja import Schema, FilterSchema, Field
from datetime import datetime, date
from typing import Optional
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
    
class FiltersSchema(FilterSchema):
    descricao: Optional[str] = None
    custo: Optional[float] = None
    preco_revenda: Optional[float] = None
    data_validade: Optional[date] = None
    estoque: Optional[int] = None
    data_criacação: Optional[datetime] = None