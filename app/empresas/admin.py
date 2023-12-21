from django.contrib import admin
from app.empresas.models import Empresas

class EmpresasAdmin(admin.ModelAdmin):
    list_display =[
                "cnpj",
                "razao_social",
                "data_cadastro",
                "deleted",
                ]

admin.site.register(Empresas, EmpresasAdmin)