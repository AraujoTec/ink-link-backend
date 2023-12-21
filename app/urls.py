from django.contrib import admin
from django.urls import include, path

import app.api as apps

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', apps.api.urls)
]
