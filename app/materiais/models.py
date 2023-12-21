from django.db import models
from app.empresas.models import Empresas

class BaseModel(models.Model):
    class Meta:
        abstract = True

    def soft_delete(self):
        self.deleted = True
        self.save()   
          
class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter() 
       
class Materiais(BaseModel):
    descricao = models.CharField(max_length=100)
    custo = models.IntegerField()
    preco_revenda = models.IntegerField()
    empresas = models.ForeignKey(Empresas, on_delete=models.CASCADE)

    class Meta:
        db_table = "materiais"
        verbose_name = "material"
        verbose_name_plural = "materiais"

    def __str__(self):     
        return f'{self.id} - {self.descricao.title()}'
    


