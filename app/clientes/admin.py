from django.contrib import admin
from app.clientes.models import Clientes
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from app.authenticate.forms import CustomUserChangeForm, CustomUserCreationForm, GroupAdminForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Clientes
    list_display = (
                    "first_name",
                    "last_name",
                    "cpf",
                    "instagram",
                    "servico",
                    "empresa"
                    )

    fieldsets = (
                    (None, {"fields": ( 
                                        "email",                       
                                        "first_name",
                                        "last_name",
                                        "cpf",
                                        "data_nascimento",
                                        "instagram",
                                        "empresa",
                                        "cep",
                                        "telefone",
                                        "servico",
                                        "colaborador",
                                        "forma_pagamento",                                      
                                        )}),
                    ("Permissions", {"fields": (("is_active"), "groups")}),
                    ('Password Details',{'fields' : ('password',)}),
                )
    add_fieldsets = (
                    (None,{"classes": ("wide",),
                    "fields": (
                                "email",
                                "first_name",
                                "last_name",
                                "password1",
                                "password2",
                                "cpf",
                                "data_nascimento",
                                "instagram",
                                "empresa",
                                "cep",
                                "telefone",
                                "servico",
                                "colaborador",
                                "forma_pagamento",                                      
                                "is_active",
                             ),
                            },
                     ),
                    )
    
    search_fields = ("email","empresa","cpf","colaborador")
    ordering = ("email",)


class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    filter_horizontal = ["permissions"]
    search_fields = ("name",)
    list_filter = ("name",)


admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
admin.site.register(Clientes, CustomUserAdmin)
