from django.contrib import admin
from app.materiais.models import Materiais


class MateriaisAdmin(admin.ModelAdmin):
    list_display =[
                "descricao",
                "empresa",
                "estoque"
                ]

admin.site.register(Materiais, MateriaisAdmin)