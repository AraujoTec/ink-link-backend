from django.contrib import admin
from django.urls import path
from app.materiais import views

urlpatterns = [
    path('/', views.get_itens, name="get_all_itens"),
    path('/<int:item_id>/', views.get_item_by_id)
]