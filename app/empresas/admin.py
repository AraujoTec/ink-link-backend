from django.contrib import admin
from app.empresas.models import Empresas

class EmpresasAdmin(admin.ModelAdmin):
    list_display =[
                "razao_social",
                "cnpj",
                "data_cadastro",
                "deleted",
                ]

admin.site.register(Empresas, EmpresasAdmin)