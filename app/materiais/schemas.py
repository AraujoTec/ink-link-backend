from ninja import Schema
from datetime import date

class MateriaisSchema(Schema):
    descricao: str
    custo: float
    preco_revenda: float
    empresas: str
    data_validade: date = None
    estoque: int