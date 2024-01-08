from django.contrib import admin
from app.usuarios.models import Usuarios
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from app.authenticate.forms import CustomUserChangeForm, CustomUserCreationForm, GroupAdminForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuarios
    list_display = (
                    "email",
                    "first_name",
                    "last_name",
                    "cpf",
                    "cargo",
                    "empresa"
                    )

    fieldsets = (
                    (None, {"fields": ( 
                                        "email",                       
                                        "first_name",
                                        "last_name",
                                        "cpf",
                                        "data_nascimento",
                                        "empresa",
                                        "cargo",                                   
                                        )}),
                    ("Permissions", {"fields": ("is_staff", "is_active")}),
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
                                "empresa",
                                "cargo",                                      
                                "is_active",
                                "groups",
                             ),
                            },
                     ),
                    )
    
    search_fields = ("email","cargo","cpf")
    ordering = ("email",)


class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    filter_horizontal = ["permissions"]
    search_fields = ("name",)
    list_filter = ("name",)


admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
admin.site.register(Usuarios, CustomUserAdmin)
