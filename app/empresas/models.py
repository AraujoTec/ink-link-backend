from django.db import models
from datetime import datetime

class Empresas(models.Model):
    razao_social = models.CharField(max_length=200, default='')
    nome_fantasia = models.CharField(max_length=200, default='')
    cnpj = models.CharField(max_length=14, default='')
    telefone = models.CharField(max_length=11, default='')
    user_criacao = models.CharField(max_length=200, default='')
    user_alteracao = models.CharField(max_length=200, default='')
    data_cadastro = models.DateTimeField(default=datetime.now())
    data_atualizacao = models.DateTimeField(default=None)
    excluido = models.BooleanField(default=False)
    
    class Meta:
        db_table = "empresas"
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
    
    def __str__(self):
        return f"{self.razao_social} - {self.cnpj}"  