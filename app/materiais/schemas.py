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
    data_criacao: datetime = datetime.now()
    
class FiltersSchema(FilterSchema):
    descricao: Optional[str] = Field(None, q='descricao__icontains')
    custo: Optional[float] = None
    preco_revenda: Optional[float] = None
    data_validade: Optional[date] = Field(None, q='data_validade__icontains')
    estoque: Optional[int] =Field(None, q='estoque__icontains')
    data_criacao: Optional[datetime] =Field(None, q='data_criacao__icontains')