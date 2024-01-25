from ninja import Router
from app.payments.service import PaymentService
from app.payments.schemas import PaymentSchema, PaymentSchemaOut
from app.authenticate.service import JWTAuth

payments_router = Router(auth=JWTAuth(), tags=['Formas de Pagamento'])
 
 
#GETS
@payments_router.get("", response=list[PaymentSchemaOut])
def get_payment(request):
    service = PaymentService(request)
    return service.get_payment()    
    

#POST
@payments_router.post("payments")
def create_payment(request, payload: PaymentSchema):
    service = PaymentService(request)
    return service.create_payment(payload)
    

#DELETE
@payments_router.delete("{payment_id}")
def delete_payment(request, payment_id: str):
    service = PaymentService(request)
    return service.delete_payment(payment_id)
    

