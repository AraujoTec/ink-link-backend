from django.contrib import admin
from django.urls import path, include
from app.usuarios import views

urlpatterns = [
    path('/', views.get_user, name="get_all_user"),
    path('/<int:user_id>/', views.get_users_by_id)
]