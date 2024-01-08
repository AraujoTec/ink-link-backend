from ninja import Schema
from uuid import UUID

class PaymentSchema(Schema):
    forma_pagamento: str
    
class PaymentSchemaOut(PaymentSchema):
    id: UUID
    empresa_id: UUID