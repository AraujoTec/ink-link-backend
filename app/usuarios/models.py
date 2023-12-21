from django.db import models
from app.empresas.models import Empresas 
from app.authenticate.models import User

FUNCOES_CHOICES = [
    ('ADM', "Administrativo"),
    ('RECP', "Recepcao"),
    ('TAT', "Tatuador"),
    ('BODY', "Body Piercing"),
    ('MIC', "Micropigmentação")
    ]

class BaseModel(models.Model):
    deleted = models.BooleanField(default=False)
    class Meta:
        abstract = True

    def soft_delete(self):
        self.deleted = True
        self.is_active = False 
        self.save()    
class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)          
class Usuarios(User, BaseModel):
        
    data_nascimento = models.DateField(default=None, null=True, blank=True)
    funcao = models.CharField(max_length=100, choices=FUNCOES_CHOICES)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)

    class Meta:
        db_table = "usuarios"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.cpf}'