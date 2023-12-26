from django.db import models
from app.materiais.models import Materiais
from app.servicos.models import Servicos
import uuid

class Detalhes(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    materiais = models.ForeignKey(Materiais, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0, blank=False)
    valor_total=models.CharField(max_length=100, default="0")
    lucro_estudio=models.CharField(max_length=100, default="0", blank=True, null=None)
    lucro_colaborador=models.CharField(max_length=100, default="0", blank=True, null=None)


    class Meta:
        db_table = "detalhes"
        verbose_name = "Detalhamento"
        verbose_name_plural = "Detalhamentos"
    
    def __str__(self):
        return f"{self.servico} - {self.materiais} - {self.quantidade}"  
