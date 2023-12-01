from django.contrib import admin
from django.urls import include, path
from app.empresas import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("empresas/", include("app.empresas.urls"), name="empresa_urls"),
    path('api/', views.api.urls)
]