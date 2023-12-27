from django.http import JsonResponse
from app.payments.models import Payments
from app.payments.schemas import  PaymentSchema
from app.utils.jwt_manager import authenticate

class PaymentService:
    def get_payment(self, empresa_id: str):
        return Payments.objects.filter(empresa_id=empresa_id) 

    def create_payment(self,request, payload: PaymentSchema):
        
        token = authenticate(request)
                
        if Payments.objects.filter(payment=payload.forma_pagamento, empresa_id=token.get("empresa_id")):
            return JsonResponse(data={'error': "Forma de pagamento já cadastrada"}, status=400) 
        
        
        dados = payload.dict()
        dados["empresa_id"] = token.get("empresa_id")
        
        payment = Payments.objects.create(**dados)
        return JsonResponse(data={"sucess": f'{"Forma de pagamento criada com sucesso"} - {payment.id}'}, status=200)
    
    def delete_payment(self, request, payment_id: str):
        token = authenticate(request)
        
        payment = Payments.objects.filter(id=payment_id, empresa_id=token.get("empresa_id"))
        payment.delete()
        return JsonResponse(data={"sucess": "Forma de pagamento excluida com sucesso"}, status=200)
