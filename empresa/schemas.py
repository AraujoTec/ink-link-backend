from rest_framework import serializers
from .models import Empresa
from ninja import Schema
from datetime import datetime

class EmpresaSchema(Schema):
    id: int
    razao_social: str
    nome_fantasia: str
    cnpj: str
    telefone: str
    user_criacao: str
    user_alteracao: str
    data_cadastro: datetime = None
    data_atualizacao: datetime = None
    excluido: bool
    