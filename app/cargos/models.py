from django.db import models
import uuid

class Cargos(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cargo = models.CharField(max_length=200)    
    empresa_id = models.CharField(max_length=200)
    
    
    class Meta:
        db_table = "cargo"
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
        
    def __str__(self):
        return self.id
    
    