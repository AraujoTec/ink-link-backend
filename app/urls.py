from django.contrib import admin
from django.urls import include, path

import app.api as apps

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', apps.api.urls),
    path("empresas/", include("app.empresas.urls"), name="empresa_urls"),
    path("users/", include("app.usuarios.urls"), name="users_urls")
]
