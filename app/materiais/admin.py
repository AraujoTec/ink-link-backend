from django.contrib import admin
from app.materiais.models import Materiais

admin.site.register(Materiais)

class MateriaisAdmin(admin.ModelAdmin):
    list_display =[
                "item_id",
                "descrição",
                "custo",
                "preço_revenda",
                "empresas_id",
                "deleted"
                ]
