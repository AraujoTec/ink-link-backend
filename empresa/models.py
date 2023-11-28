from django.db import models
from datetime import datetime

class Empresa(models.Model):
    razao_social = models.CharField(max_length=200)
    nome_fantasia = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14)
    telefone = models.CharField(max_length=11)
    user_criacao = models.CharField(max_length=200)
    user_alteracao = models.CharField(max_length=200)
    data_cadastro = models.DateTimeField(default=datetime.now())
    data_atualizacao = models.DateTimeField(default=None)
    excluido = models.BooleanField(default=False)