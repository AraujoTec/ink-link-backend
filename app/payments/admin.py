from django.contrib import admin
from app.payments.models import Payments

class PaymentsAdmin(admin.ModelAdmin):
    list_display =[
                "forma_pagamento",
                "id",
                "empresa",
                ]


admin.site.register(Payments, PaymentsAdmin)