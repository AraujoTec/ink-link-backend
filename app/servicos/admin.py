from django.contrib import admin
from app.servicos.models import Servicos

class ServicosAdmin(admin.ModelAdmin):
    list_display =[
                "servico",
                "id",
                "empresa",
                ]

admin.site.register(Servicos, ServicosAdmin)