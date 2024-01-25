from django.http import JsonResponse
from app.payments.models import Payments
from app.payments.schemas import  PaymentSchema
from app.utils.jwt_manager import authenticate

class PaymentService:
    
    def __init__(self, request):
        self.token = authenticate(request)    
        self.empresa = self.token.get("empresa_id")
            
    def get_payment(self ):
        return Payments.objects.filter(empresa_id=self.empresa) 

    def create_payment(self, payload: PaymentSchema):
                       
        if Payments.objects.filter(payment=payload.forma_pagamento, empresa_id=self.empresa):
            return JsonResponse(data={'error': "Forma de pagamento já cadastrada"}, status=400) 
                
        dados = payload.dict()
        dados["empresa_id"] = self.empresa
        
        payment = Payments.objects.create(**dados)
        return JsonResponse(data={"sucess": f'{"Forma de pagamento criada com sucesso"} - {payment.id}'}, status=200)
    
    def delete_payment(self,  payment_id: str):
        payment = Payments.objects.filter(id=payment_id, empresa_id=self.empresa)
        payment.delete()
        return JsonResponse(data={"sucess": "Forma de pagamento excluida com sucesso"}, status=200)
