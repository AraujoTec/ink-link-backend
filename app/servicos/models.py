from django.db import models
from django.db import models
from app.empresas.models import Empresas
import uuid

class Servicos(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    servico = models.CharField(max_length=200)    
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    
    
    class Meta:
        db_table = "servico"
        verbose_name = "Servico"
        verbose_name_plural = "Servicos"
        
    def __str__(self):
        return str(self.servico)
    
    