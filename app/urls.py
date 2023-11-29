from django.contrib import admin
from django.urls import include, path
from empresa import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("empresas/", include("empresa.urls"), name="empresa_urls"),
    path('api/', views.api.urls)
]