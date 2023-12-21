from ninja import Schema


class MateriaisSchema(Schema):
    descricao: str
    custo: float
    preco_revenda: float
    empresas_id: str
