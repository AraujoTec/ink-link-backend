from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_empresa, name="get_all_empresas"),
    path('/<int:empresa_id>', views.get_by_id)
]