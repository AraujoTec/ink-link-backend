from django.db import models
from django.contrib.auth import get_user_model
from app.empresas.models import Empresas
import uuid
class BaseModel(models.Model):
    deleted = models.BooleanField(default=False)
    class Meta:
        abstract = True

    def soft_delete(self):
        self.deleted = True
        self.save()     
class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)    
class Usuarios(get_user_model(), BaseModel):
      
    FUNCOES_CHOICES = [
        ('ADM', "Administrativo"),
        ('RECP', "Recepcao"),
        ('TAT', "Tatuador"),
        ('BODY', "Body Piercing"),
        ('MIC', "Micropigmentação")
    ]
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data_nascimento = models.DateField(default=None)
    funcao = models.CharField(max_length=100, choices=FUNCOES_CHOICES)
    cpf = models.CharField(max_length=11)
    empresas = models.ForeignKey(Empresas, on_delete=models.CASCADE)
   
    class Meta:
        db_table = "usuarios"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):     
        return f'{self.first_name.title()} {self.last_name.title()} - {self.cpf.strip(".")}'
    
