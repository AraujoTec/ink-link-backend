from django.db import models
from app.empresas.models import Empresas
from app.usuarios.models import Usuarios
from app.detalhe_servico.models import Detalhes
from app.payments.models import Payments
from app.clientes.models import Clientes
import uuid

class Agendamento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    colaborador = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    detalhes = models.ForeignKey(Detalhes, on_delete=models.CASCADE)
    data_agendamento=models.DateField(blank=True, null=None)
    data_pagamento=models.DateField(blank=True, null=None)
    forma_pagamento = models.ForeignKey(Payments, on_delete=models.CASCADE)
    
          
    class Meta:
        db_table = "agendamento"
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
    
    def __str__(self):
        return f"{self.cliente}"  
