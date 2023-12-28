from django.contrib import admin
from app.usuarios.models import Usuarios
class UsuariosAdmin(admin.ModelAdmin):
    list_display =[
                "first_name",
                "last_name",
                "email",
                "data_nascimento",
                "empresa_id",
                ]

admin.site.register(Usuarios, UsuariosAdmin)
