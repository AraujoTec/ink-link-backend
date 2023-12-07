from django.contrib import admin
from app.empresas.models import Empresas

admin.site.register(Empresas)
class EmpresasAdmin(admin.ModelAdmin):
    list_display =[
                "uuid",
                "razao_social",
                "nome_fantasia",
                "cnpj",
                "telefone",
                "user_criacao",
                "user_alteracao",
                "data_cadastro",
                "data_atualizacao",
                "excluido",
                ]
