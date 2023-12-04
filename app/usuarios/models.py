from django.db import models
from django.contrib.auth import get_user_model
from app.empresas.models import Empresas
    
class Usuarios(get_user_model(), models.Model):
      
    FUNCOES_CHOICES = [
        ('ADM', "Administrativo"),
        ('RECP', "Recepcao"),
        ('TAT', "Tatuador"),
        ('BODY', "Body Piercing"),
        ('MIC', "Micropigmentação")
    ]

    data_nascimento = models.DateField(default=None)
    funcao = models.CharField(max_length=100, choices=FUNCOES_CHOICES)
    cpf = models.CharField(max_length=11)
    empresa_id = models.CharField(max_length=256)
    empresas = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    
    
    class Meta:
        db_table = "usuarios"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
    
    def __str__(self):
        return self.cpf
