from django.db import models
from app.empresas.models import Empresas
import uuid

class Payments(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    forma_pagamento = models.CharField(max_length=200)    
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    
    
    class Meta:
        db_table = "forma_pagamento"
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
        
    def __str__(self):
        return str(self.forma_pagamento)
    
    