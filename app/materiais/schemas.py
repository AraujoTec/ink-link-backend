from ninja import Schema
from datetime import date

class MateriaisSchema(Schema):
    descricao: str
    custo: float
    preco_revenda: float
    empresa_id: str
    data_validade: date = None
    estoque: int