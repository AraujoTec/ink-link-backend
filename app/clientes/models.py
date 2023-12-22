from django.db import models
from app.mixins.base_model import BaseModel
from app.authenticate.models import User
from app.servicos.models import Servicos
from app.usuarios.models import Usuarios
from app.payments.models import Payments


class Clientes(User, BaseModel):
        
    cpf = models.CharField(max_length=11, null=False, blank=False)
    data_nascimento = models.DateField(default=None, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=None, blank=True)
    cep = models.CharField(max_length=8, null=None, blank=True)
    telefone = models.CharField(max_length=11)
    servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    forma_pagamento = models.ForeignKey(Payments, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "clientes"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.cpf}'