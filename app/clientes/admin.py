from django.contrib import admin
from app.clientes.models import Clientes

class ClientesAdmin(admin.ModelAdmin):
    list_display = [
                    "first_name",
                    "last_name",
                    "cpf",
                    "instagram",
                    "servico",
                    ]

admin.site.register(Clientes)
