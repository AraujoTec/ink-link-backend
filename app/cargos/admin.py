from django.contrib import admin
from app.cargos.models import Cargos


class CargosAdmin(admin.ModelAdmin):
    list_display =[
                "cargo",
                "id",
                "empresa",
                ]

admin.site.register(Cargos, CargosAdmin)