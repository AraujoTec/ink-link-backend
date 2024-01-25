from ninja import Schema, FilterSchema, Field
from uuid import UUID
from datetime import date
from typing import Optional
class AgendaBase(Schema):
    cliente_id: UUID
    empresa_id: UUID
    colaborador_id: UUID
    detalhes_servico_id: UUID
    data_agendamento: date
    data_pagamento: date
    forma_pagamento_id: UUID

class AgendaSchemaOut(AgendaBase):
    id: UUID
    
class FiltersSchema(FilterSchema):
    id: Optional[UUID] = None
    cliente_id: Optional[UUID] = None
    empresa_id: Optional[UUID] = None
    colaborador_id: Optional[UUID] = None
    detalhes_servico_id: Optional[UUID] = None
    data_agendamento: Optional[date] = Field(None, q='data_agendamento__icontains')
    data_pagamento: Optional[date] = Field(None, q='data_pagamento__icontains')
    forma_pagamento_id: Optional[UUID] = None
    