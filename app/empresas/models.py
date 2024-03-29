from app.mixins.base_model import BaseModel
from django.db import models
from datetime import datetime
import uuid
class Empresas(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    razao_social = models.CharField(max_length=200, default='')
    nome_fantasia = models.CharField(max_length=200, default='')
    cnpj = models.CharField(max_length=14, default='')
    telefone = models.CharField(max_length=11, default='')
    user_alteracao = models.CharField(max_length=200, blank=True, null=None)
    data_cadastro = models.DateTimeField(default=datetime.now())
    data_atualizacao = models.DateTimeField(default=datetime.now())
    
    class Meta:
        db_table = "empresa"
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
    
    def __str__(self):
        return f"{self.razao_social} - {self.cnpj}"  