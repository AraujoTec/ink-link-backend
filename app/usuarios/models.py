from django.db import models
from app.mixins.base_model import BaseModel
from app.authenticate.models import User
from app.cargos.models import Cargos

class Usuarios(User, BaseModel):
        
    data_nascimento = models.DateField(default=None, null=True, blank=True)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE)

    class Meta:
        db_table = "colaborador"
        verbose_name = "colaborador"
        verbose_name_plural = "Colaboradores"
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.cargo}'