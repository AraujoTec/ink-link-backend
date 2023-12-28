from ninja import Schema
from uuid import UUID

class CargoSchema(Schema):
    cargo: str
    
class CargoSchemaOut(CargoSchema):
    id: UUID
    empresa_id: UUID