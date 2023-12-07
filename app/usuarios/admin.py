from django.contrib import admin
from app.usuarios.models import Usuarios

admin.site.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display =[
                "username",
                "first_name",
                "last_name",
                "funcao",
                "cpf",
                "uuid",
                "data_nascimento",   
                "is_staff",
                "empresas_id",
                "email",
                "password",  
                "is_superuser",
                "is_active",
                "last_login",
                "date_joined",
                "deleted"
                ]
