from django.db import models
from app.empresas.models import Empresas

class Materiais(models.Model):
    descricao = models.CharField(max_length=100)
    custo = models.IntegerField()
    preco_revenda = models.IntegerField()
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    data_validade = models.DateField(default = None)
    estoque = models.IntegerField()
    class Meta:
        db_table = "materiais"
        verbose_name = "material"
        verbose_name_plural = "materiais"

    def __str__(self):     
        return f'{self.id} - {self.descricao.title()}'
    


