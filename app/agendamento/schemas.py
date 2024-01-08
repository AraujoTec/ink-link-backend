from ninja import Schema
from uuid import UUID
from datetime import date

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
