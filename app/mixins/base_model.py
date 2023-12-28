from django.db import models

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